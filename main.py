from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("home_page.html")


@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
