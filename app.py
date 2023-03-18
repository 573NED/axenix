from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    with open('cresult.txt', 'r') as file:
        content = file.read()
    return render_template('index.html', content=content)

if __name__ == "__main__":
    app.run(debug=True)