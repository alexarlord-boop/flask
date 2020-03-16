from flask import Flask, render_template, redirect
from form import RegisterForm
from data import db_session, users, jobs
from data.users import User
from data.jobs import Jobs
import json

# from data.news import News

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

with open("data/col.json") as f:
    colonials = json.load(f)["crew"]
with open("data/jobs.json") as f:
    jb = json.load(f)["jobs"]


def create_user(params, session):
    us = User()

    us.surname = params['surname']
    us.name = params['name']
    us.age = params['age']
    us.position = params['position']
    us.speciality = params['speciality']
    us.address = params['address']
    us.email = params['email']

    session.add(us)
    session.commit()


def create_job(params, session):
    job = Jobs()

    job.team_leader = params["team_leader"]
    job.job = params["job deployment"]
    job.work_size = params["work_size"]
    job.collaborators = params["collaborators"]
    job.start_date = params["start_date"]
    job.is_finished = params["is_finished"]
    session.add(job)
    session.commit()


def main():
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()

    for i, person_params in colonials.items():
         create_user(person_params, session)

    for i, job_params in jb.items():
        print(job_params)
        create_job(job_params, session)

    app.run()


@app.route("/")
def index():
    session = db_session.create_session()
    job = session.query(Jobs).all()
    return render_template("index.html", job=job)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    main()
