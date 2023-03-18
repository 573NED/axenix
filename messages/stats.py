import os
import csv

# Путь к папке с CSV файлами
folder_path = ()

# Путь к папке для сохранения файлов со статистикой
stats_path = os.path.join('', "stats")

# Создаем папку, если она не существует
if not os.path.exists(stats_path):
    os.mkdir(stats_path)

# Проходим по всем файлам в папке
for filename in os.listdir():
    if filename.endswith(".csv"):
        # Открываем CSV файл для чтения
        with open(os.path.join( filename), "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Пропускаем заголовок

            # Создаем словарь, где ключами будут являться адреса отправителей,
            # а значениями - количество сообщений от них
            message_counts = {}
            for row in reader:
                sender = row[0]
                if sender not in message_counts:
                    message_counts[sender] = 0
                message_counts[sender] += 1

        # Создаем имя нового файла, добавляя к исходному имени флаг "qq"
        new_filename = os.path.splitext(filename)[0] + "_qq.csv"

        # Открываем новый CSV файл для записи в папке "stats"
        with open(os.path.join(stats_path, new_filename), "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Sender", "Message count"])

            # Записываем статистику в новый файл
            for sender, count in message_counts.items():
                writer.writerow([sender, count])