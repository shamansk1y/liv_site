import bs4
import logging
import csv
import requests
from fake_useragent import UserAgent
import collections
import time
import re

logger = logging.getLogger('livesta')
logging.basicConfig(level=logging.INFO)

ua = UserAgent()
headers = {'User-Agent': ua.random}
ParseResult = collections.namedtuple(
    'ParseResult',
    (
        'name',
        'url',
        'price_old',
        'price_new',
        'image',
        'description',
        'article',
        'brand',
        'weight',
        'country',
        'application',
        'warning',
        'consist',
        'status',

    ),
)

HEADERS = (
    'name',
    'url',
    'price_old',
    'price_new',
    'image',
    'description',
    'article',
    'brand',
    'weight',
    'country',
    'application',
    'warning',
    'consist',
    'status',
)


class Client:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = headers
        self.result = []
        self.start_time = None
        self.total_time = None
        self.timeout = 10  # Тайм-аут в секундах

    def load_page(self, page):
        url = f'https://livesta.com.ua/index.php?route=product/search&for=&page={page}'
        res = self.session.get(url, timeout=self.timeout)
        res.raise_for_status()
        return res.content

    def parse_page(self, html):
        soup = bs4.BeautifulSoup(html, 'html.parser')
        cards = soup.select('.product-wrapper')

        if not cards:
            return False

        for card in cards:
            # Извлекаем основную информацию о товаре
            goods_name_elem = card.select_one('.name a')
            name = goods_name_elem.text.strip()
            url = goods_name_elem['href']

            price_new_elem = card.select_one('.prices .price')
            if price_new_elem:
                price_new_text = price_new_elem.text.strip()
                price_new_match = re.search(r'(\d+\.\d+)', price_new_text)
                price_new = price_new_match.group(1) if price_new_match else None

                price_old_elem = card.select_one('.prices .through')
                if price_old_elem:
                    price_old_text = price_old_elem.text.strip()
                    price_old_match = re.search(r'(\d+\.\d+)', price_old_text)
                    price_old = price_old_match.group(1) if price_old_match else None
                else:
                    price_old = None
            else:
                price_new = None
                price_old = None

            # Парсим дополнительную информацию с URL товара
            additional_info = self.parse_additional_info(url)

            # Создаем экземпляр ParseResult и добавляем его в список результатов
            self.result.append(ParseResult(
                name=name,
                url=url,
                price_old=price_old,
                price_new=price_new,
                image=additional_info['image'],
                description=additional_info['description'],
                article=additional_info['article'],
                brand=additional_info['brand'],
                weight=additional_info['weight'],
                country=additional_info['country'],
                application=additional_info['application'],
                warning=additional_info['warning'],
                consist=additional_info['consist'],
                status=additional_info['status'],

            ))

        return True

    def parse_additional_info(self, url):
        res = self.session.get(url, timeout=self.timeout)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.content, 'html.parser')

        div_element = soup.find('div', class_='photo __preview_state_zoom')
        img_element = div_element.find('img')
        image = img_element['src']

        description = ''
        article = ''
        brand = ''
        weight = ''
        country = ''
        application = ''
        warning = ''
        consist = ''
        status = ''  # Добавлено значение по умолчанию для переменной status

        div_element = soup.find('div', class_='description info')
        if div_element:
            p_elements = div_element.find_all('p')
            description = '\n'.join([p.get_text() for p in p_elements])

        art_el = soup.select_one('.preview-wrapper')
        if art_el:
            article = art_el.select_one('.sku').text

        characteristics = soup.find('div', {'id': 'attribute'})
        if characteristics:
            application_element = characteristics.find('span', string='Застосування')
            if application_element:
                application = application_element.find_next_sibling('span')
                if application:
                    application = application.text.strip()

            brand_element = characteristics.find('span', string='Бренд')
            if brand_element:
                brand = brand_element.find_next_sibling('span').text.strip()

            weight_element = characteristics.find('span', string='Вага')
            if weight_element:
                weight = weight_element.find_next_sibling('span').text.strip()

            country_element = characteristics.find('span', string='Країна виробництва')
            if country_element:
                country = country_element.find_next_sibling('span').text.strip()

            warning_element = characteristics.find('span', string='Застереження')
            if warning_element:
                warning = warning_element.find_next_sibling('span')
                if warning:
                    warning = warning.text.strip()

            consist_element = characteristics.find('span', string='Склад')
            if consist_element:
                consist = consist_element.find_next_sibling('span')
                if consist:
                    consist = consist.text.strip()

        status_element = soup.find('div', class_='stock')
        if status_element:
            status_label = status_element.find('div', class_='label')
            status_value = status_element.find('span', class_='in-stock')
            if status_label and status_value:
                status = status_value.text.strip()

        additional_info = {
            'image': image,
            'description': description,
            'article': article,
            'brand': brand,
            'weight': weight,
            'country': country,
            'application': application,
            'warning': warning,
            'consist': consist,
            'status': status,
        }
        return additional_info

    def save_results(self):
        with open('livesta_product.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)
            for item in self.result:
                writer.writerow(item)

    def run(self):
        logger.info('Загрузка страницы...')
        page = 1
        self.start_time = time.time()

        while True:
            logger.info(f'Парсинг страницы {page}...')
            html = self.load_page(page)
            has_next_page = self.parse_page(html)
            logger.info(f'Сохранение результатов страницы {page}...')

            # Засекаем время отработки и выводим в терминал
            elapsed_time = time.time() - self.start_time
            logger.info(f'Время парсинга текущей страницы: {elapsed_time:.2f} секунд')

            self.save_results()

            if not has_next_page:
                self.total_time = time.time() - self.start_time
                logger.info(f'Общее время парсинга всех страниц: {self.total_time:.2f} секунд')
                break

            page += 1
            time.sleep(3)  # Тайм-аут в 3 секунды

        logger.info('Готово!')


if __name__ == '__main__':
    client = Client()
    client.run()
