from flask import Flask

app = Flask(__name__)

@app.route('/')
def name():
    return 'Миссия Колонизация Марса'

@app.route('/index')
def motto():
    return 'И на Марсе будут яблони цвести!'

@app.route('/promotion')
def promo():
    return 'Человечество вырастает из детства.</br></br>Человечеству мала одна планета.</br></br>Мы сделаем обитаемыми безжизненные пока планеты.</br></br>И начнем с Марса!</br></br>Присоединяйся!'

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')