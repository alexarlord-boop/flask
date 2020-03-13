from flask import Flask, render_template, redirect
from form import RegisterForm
from data import db_session, news, users
from data.users import User
from data.news import News

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

user1 = {
    "name": "Пользователь 1",
    "about": "биография пользователя 1",
    "email": "email1@email.ru",
    "pass": None
}
user2 = {
    "name": "Пользователь 2",
    "about": "биография пользователя 2",
    "email": "email2@email.ru",
    "pass": None
}
user3 = {
    "name": "Пользователь 3",
    "about": "биография пользователя 3",
    "email": "email3@email.ru",
    "pass": None
}


def create_user(params, session):
    user = User()
    user.name = params["name"]
    user.about = params["about"]
    user.email = params["email"]
    user.hashed_password = params["pass"]
    session.add(user)
    session.commit()


def main():
    db_session.global_init("db/blogs.sqlite")
    session = db_session.create_session()
    # create_user(params=user1, session=session)
    # create_user(params=user2, session=session)
    # create_user(params=user3, session=session)

    # session.query(User).filter(User.id > 1).delete()
    # session.commit()

    # news = News(title="Первая новость", content="Привет блог!",
    #             user_id=1, is_private=False)
    # session.add(news)
    session.commit()
    app.run()


@app.route("/")
def index():
    session = db_session.create_session()
    news = session.query(News).filter(News.is_private is not True)
    return render_template("index.html", news=news)


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
