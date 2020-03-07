from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def choice(planet_name):
    if planet_name == 'Марс':
        return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>promo</title>
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" href={url_for('static', filename='css/style.css')}
                  </head>
                  <body>
                  <div class="Top"><h1>Мое предлжение: Марс!</h1></div>
                            

            <div class="alert alert-info h1" role="alert">Человечество вырастает из детства.</div>
            <div class="alert alert-success h1" role="alert">Человечеству мала одна планета.</div>
            <div class="alert alert-info h1" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</div>
            <div class="alert alert-warning h1" role="alert">И начнем с Марса!</div>
            <div class="alert alert-danger h1" role="alert">Присоединяйся!</div>
                   
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
