from flask import Flask, url_for, render_template, redirect
from loginform import LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'

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
    list_data = ['Ультрамегахороши инженер', 'Крутой капитан', 'Живительный врач', 'Никому ненужный басист']
    return render_template('list.html', list_type=list, list=list_data)


@app.route('/distribution')
def list_cabins():
    list_of_cabins = ['first', 'second', 'third', 'fourth', 'fifth']
    return render_template('list_cabins.html', list=list_of_cabins)


@app.route('/answer')
def answer():
    data = dict()
    data['title'] = 'title'
    data['surname'] = 'surname'
    data['name'] = 'name'
    data['education'] = 'education'
    data['profession'] = 'profession'
    data['sex'] = 'sex'
    data['motivation'] = 'motivation'
    data['ready'] = 'ready'

    return render_template('answer.html', data=data, style=url_for('static', filename='css/style_for_answer'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login_form.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8081, host='127.0.0.1')
