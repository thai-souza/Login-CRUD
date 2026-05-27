from flask import Flask, render_template, request, redirect, url_for
from pathlib import Path
from app.config import SECRET_KEY
from app.supabase_client import supabase

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

    return render_template('index.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']


        try:
            response = supabase.auth.sign_up(
                {
                    "email" : email,
                    "password" : password
                })
                
            if response.user:
                user_id = response.user.id

                supabase.table('profiles').insert({
                    "id": user_id,
                    "first_name": first_name,
                    "last_name": last_name
                }).execute()

                return redirect('login')
        
        except Exception as e:
            print(e)  
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

