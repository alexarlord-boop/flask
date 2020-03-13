from flask import Flask
from data import db_session, news, users

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


def create_user(params):
    user = users.User()
    user.name = params["name"]
    user.about = params["about"]
    user.email = params["email"]
    user.hashed_password = params["pass"]
    session = db_session.create_session()
    session.add(user)
    session.commit()


def main():
    db_session.global_init("db/blogs.sqlite")
    create_user(params=user1)
    create_user(params=user2)
    app.run()


if __name__ == '__main__':
    main()
