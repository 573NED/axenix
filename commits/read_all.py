import pandas as pd
import os
import csv

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

# Слияние всех DataFrame в один DataFrame
merged_df = pd.concat(data_frames)

# Запись объединенного DataFrame в CSV файл
merged_df.to_csv('merged_file.csv', index=False)

commits = {}

with open('merged_file.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        author = row['author']
        message = row['commit_message']
        if 'bug' in message or 'issue' in message:
            if author in commits:
                commits[author] += 1
            else:
                commits[author] = 1

with open("сresult.txt", "w") as f:
    for author, count in sorted(commits.items(), key=lambda x: x[1], reverse=True)[:5]:
        line = f"{author}: {count} коммитов содержащих триггер\n"
        f.write(line)
        print(line, end="")