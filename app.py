from flask import Flask, render_template

app = Flask(__name__)

# Создаем список с данными для отображения
commits = [
    ('aivanov', 99),
    ('okozlova', 86),
    ('dsmisnov', 80),
    ('knikolaeva', 80),
    ('ekuznetsova', 77),
]

@app.route('/')
def index():
    return render_template('commits.html', commits=commits)

if __name__ == '__main__':
    app.run()
