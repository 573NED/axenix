import random
import csv
import datetime
from datetime import datetime, timedelta

users = ["abelov", "aivanov", "dsmisnov", "ekuznetsova", "knikolaeva", "lvasiliev", "mpetrova", "nsokolov", "okozlova", "pzaitsev"]
commit_messages = ["fix bugs", "fix bug", "fix issue", "fix bug in module",  "add feature", "refactor code", "update documentation", "optimize performance", "improve user experience", "implement new design", "add unit tests", "update dependencies"]

def generate_author():
    return random.choice(users)

def generate_commit_id():
    return "".join(random.choices("0123456789abcdef", k=7))

def generate_commit_time():
    now = datetime.now()
    a = now - timedelta(days=1)
    b = now
    rand_time = random.random() * (b - a).total_seconds()
    commit_time = a + timedelta(seconds=rand_time)
    while commit_time.hour >= 2 and commit_time.hour < 7:
        rand_time = random.random() * (b - a).total_seconds()
        commit_time = a + timedelta(seconds=rand_time)
    return commit_time.strftime("%Y-%m-%d %H:%M:%S")


def generate_commit_message():
    return random.choice(commit_messages)

#today = datetime.today().strftime('%Y-%m-%d')
today = datetime.today().strftime('%H_%M_%S')
filename = f"commits_{today}.csv"
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["commit_id", "commit_time", "commit_message", "author"])
    n_commits = random.randint(25, 50)
    for i in range(n_commits):
        writer.writerow([generate_commit_id(), generate_commit_time(), generate_commit_message(), generate_author()])