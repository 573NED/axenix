import csv
import random
from datetime import datetime, timedelta

# список пользователей
users = ["abelov", "aivanov", "dsmisnov", "ekuznetsova", "knikolaeva", "lvasiliev", "mpetrova", "nsokolov", "okozlova", "pzaitsev"]

# функция для генерации случайной даты и времени в формате "%Y-%m-%d %H:%M:%S"
def generate_timestamp():
    now = datetime.now()
    a = now - timedelta(days=1)
    b = now
    rand_time = random.random() * (b - a).total_seconds()
    commit_time = a + timedelta(seconds=rand_time)
    while commit_time.hour >= 2 and commit_time.hour < 7:
        rand_time = random.random() * (b - a).total_seconds()
        commit_time = a + timedelta(seconds=rand_time)
    return commit_time.strftime("%Y-%m-%d %H:%M:%S")


# задаем количество сообщений для генерации
n_messages = random.randint(25, 50)


# генерируем случайные данные
messages = []
for i in range(n_messages):
    sender = random.choice(users) + "@gmail.com"
    receiver = random.choice([user for user in users if user != sender[:-10]]) + "@gmail.com"
    timestamp = generate_timestamp()
    messages.append([sender, receiver, timestamp])

# сохраняем данные в csv файл
today = datetime.today().strftime('%H_%M_%S')
filename = f"mssgs_{today}.csv"
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Sender", "Receiver", "Timestamp"])
    writer.writerows(messages)