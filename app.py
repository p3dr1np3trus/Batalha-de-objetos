from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '🔥 Bem-vindo à Batalha de Objetos! 🔥'

@app.route('/batalhar')
def batalha():
    return '⚔️ A batalha começou!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
