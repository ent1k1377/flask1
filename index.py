from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
