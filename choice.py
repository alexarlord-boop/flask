from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def choice(nickname, level, rating):
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
                  <div class="Top"><h1>Результат отбора</h1></div>
                  <div class="Top h2">Претендента на участие в миссии {nickname}</div>
                            
            
            <div class="alert alert-success h1" role="alert">Ваш рейтинг после {level} этапа отбора</div>
            <div class="h3">составляет {rating}</div>
            <div class="alert alert-warning h1" role="alert">Удачи!</div>
            
                   
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

# http://127.0.0.1:8080/results/Mark/44/66
