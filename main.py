from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("home_page.html")


@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof, href_for_engineer=url_for('static', filename='img/engineer.png'),
                           href_for_nonengineer=url_for('static', filename='img/nonengineer.png'))


@app.route('/list_prof/<list>')
def list_prof(list):
    list_data = ['pipi', 'papa', 'popo', 'pupu']
    return render_template('list.html', list_type=list, list=list_data)

@app.route('/distribution')
def list_cabins():
    list_of_cabins = ['first', 'second', 'third', 'fourth', 'fifth']
    return render_template('list_cabins.html', list=list_of_cabins)

if __name__ == '__main__':
    app.run(port=8088, host='127.0.0.1')
