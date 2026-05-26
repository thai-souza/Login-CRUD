from flask import Flask, render_template, request
from pathlib import Path
from app.settings import SECRET_KEY


"""
BASE_DIR
- variável que guarda a raiz do projeto para criar caminhos seguros e automáticos

Path(__file__) -> pega o caminho do arquivo atual (app.py)
.resolve() -> transforma o caminho em absoluto
.parent() -> pega a pasta onde o arquivo está
"""

BASE_DIR = Path(__file__).resolve().parent


"""
Flask(__name__): cria a aplicação Flask
template_folder: define onde estão os arquivos HTML
static_folder: define onde estão os arquivos estáticos
"""

app = Flask(__name__, template_folder= BASE_DIR / 'app' / 'templates', static_folder=BASE_DIR /'app' / 'static')


"""
SECRET KEY

Serve para o Flask proteger:
- Sessões de usuário
- Cookies
- Login
- Flash messages
- Dados temporários
"""
app.secret_key = SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user = request.form['usuario']
        pwd = request.form['senha']

    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
        
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

