import pandas as pd
import os


os.remove('merged_file.csv')

# Список файлов в директории
files = os.listdir()

# Список для хранения содержимого всех CSV файлов
data_frames = []

# Цикл по всем файлам в папке
for file in files:
    # Проверка расширения файла
    if file.endswith('.csv'):
        # Чтение CSV файла в DataFrame
        df = pd.read_csv(os.path.join('', file))
        # Добавление DataFrame в список
        data_frames.append(df)

count = 0

for filename in os.listdir():
    if filename.endswith(".csv") and filename not in ["result.csv", "merged_file.csv"]:
        count += 1

# Слияние всех DataFrame в один DataFrame
merged_df = pd.concat(data_frames)

# Запись объединенного DataFrame в CSV файл
merged_df.to_csv('merged_file.csv', index=False)

import pandas as pd

# Читаем CSV файл в DataFrame
df = pd.read_csv('merged_file.csv')

# Группируем строки по адресу отправителя и суммируем значения Message count
grouped_df = df.groupby(['Sender']).sum()

# Сортируем DataFrame по убыванию значений столбца Message count
sorted_df = grouped_df.sort_values(by='Message count', ascending=False)

# Выводим первые три строки (три наибольших значения)
top_three = sorted_df.head(5)
print(top_three.to_string())



