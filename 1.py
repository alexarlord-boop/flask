from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def mission():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route('/index')
def index():
    return "<h1>И на Марсе будут яблони цвести!</h1>"


@app.route('/promotion')
def promo():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>promo</title>
                  </head>
                  <body>
                    <h1>Человечество вырастает из детства.</h1>
                    <h1>Человечеству мала одна планета.</h1>
                    <h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>
                    <h1>И начнем с Марса!</h1>
                    <h1>Присоединяйся!</h1>
                   
                  </body>
                </html>"""


@app.route('/image_mars')
def mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                            <div>
                                <img src="{url_for('static',filename='img/mars.png')}"'''))
                                <h3>Вот она какая, красная планета.</h3>
                            </div>

                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
