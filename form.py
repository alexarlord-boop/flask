from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                    <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                              href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                              integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                              crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href={url_for('static',
                                                                             filename='css/style.css')}/>
                        <title>Пример формы</title>
                    </head>
                    <body>
                    <h1>Форма для регистрации в суперсекретной системе</h1>
                    <div>
                        <form class="login_form" method="post">
                            <input type="text" class="form-control" id="name" placeholder="Имя">
                            <input type="text" class="form-control" id="surname" placeholder="Фамилия">
                            <input type="email" class="form-control" id="email" aria-describedby="emailHelp"
                                   placeholder="Введите адрес почты" name="email">
                            <input type="text" class="form-control" id="education" placeholder="Образование">
                            <div class="form-group">
                                <label for="classSelect">Ваша профессия</label>
                                <select class="form-control" id="classSelect" name="prof">
                                    <option>инженер-исследователь</option>
                                    <option>пилот</option>
                                    <option>строитель</option>
                                    <option>экзобиолог</option>
                                    <option> врач</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label for="form-check">Укажите пол</label>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                    <label class="form-check-label" for="male">
                                        Мужской
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                    <label class="form-check-label" for="female">
                                        Женский
                                    </label>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="about">Мотивация</label>
                                <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                            </div>
                            <div class="form-group">
                                <label for="photo">Приложите фотографию</label>
                                <input type="file" class="form-control-file" id="photo" name="file">
                            </div>
                            <div class="form-group form-check">
                                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                            </div>
                            <button type="submit" class="btn btn-primary">Записаться</button>
                        </form>
                    </div>
                    </body>
                    </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
