import pandas as pd

# Загрузка CSV-файла
df = pd.read_csv('livesta_product.csv')

# Создание объекта Excel-файла
excel_file = 'livesta_product.xlsx'

# Сохранение данных в Excel
df.to_excel(excel_file, index=False)
