from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    id_astr = StringField('id астронавта', validators=[DataRequired()])
    # username = StringField('Логин', validators=[DataRequired()])
    password_astr = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_cap = StringField('id капитана', validators=[DataRequired()])
    password_cap = PasswordField('Пароль капитана', validators=[DataRequired()])
    # remember_me = BooleanField('id капитана')
    submit = SubmitField('Доступ')


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('base.html', title='Домашняя страница',
                           username=user)


@app.route('/training/<prof>')
def traning(prof):
    return render_template('prof.html', prof=prof)


@app.route('/list_prof/<lst>')
def list_prof(lst):
    prof_lst = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'климатолог',
                'штурман', 'пилот дронов']
    return render_template('list_prof.html', lst=lst, prof_lst=prof_lst)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    ans_slv = {'Фамилия': 'Watny', 'Имя': 'Mark', 'Образование': 'выше среднего',
               'Профессия': 'штурман марсохода', 'Пол': 'male',
               'Мотивация': 'Всегда мечтал застрять на Марсе!', 'Готовы остаться на Марсе?': 'True'}
    return render_template('auto_answer.html', ans_slv=ans_slv)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    list_cabin = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс',
                  'Шон Бин']
    return render_template('distribution.html', list_cabin=list_cabin)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    color = 'red'
    if age >= 21:
        age = 'ino1.png'
        if sex == 'male':
            color = '#007FF0'
        elif sex == 'female':
            color = '#FF4500'
    else:
        age = 'ino2.png'
        if sex == 'male':
            color = '#B0C4DE'
        elif sex == 'female':
            color = '#FFA07A'
    return render_template('table.html', color=color, age=age)


@app.route('/carousel')
def carousel():
    return render_template('carousel1.html')


@app.route('/member')
def member():
    import json, random
    with open('templates/f.json') as f:
        templates = json.load(f)
    n = str(random.randint(0, len(templates) - 1))
    name = templates[n]['name']
    surname = templates[n]['surname']
    path = templates[n]['path']
    jobs = ', '.join(sorted(templates[n]['jobs']))
    return render_template('member.html', name=name, surname=surname, path=path, jobs=jobs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
