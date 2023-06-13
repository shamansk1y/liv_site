var carouselItems = document.querySelectorAll('#product-carousel .carousel-inner .item');
var carouselIndicators = document.querySelectorAll('#product-carousel .carousel-indicators li');

// Устанавливаем первое изображение активным
carouselItems[0].classList.add('active');
carouselIndicators[0].classList.add('active');

// Обрабатываем клики по индикаторам
carouselIndicators.forEach(function(indicator, index) {
    indicator.addEventListener('click', function() {
        // Удаляем активные классы со всех элементов
        carouselItems.forEach(function(item) {
            item.classList.remove('active');
        });
        carouselIndicators.forEach(function(indicator) {
            indicator.classList.remove('active');
        });

        // Добавляем активные классы выбранному элементу
        carouselItems[index].classList.add('active');
        indicator.classList.add('active');
    });
});