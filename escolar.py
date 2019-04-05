# Importando as bibliotecas:

from flask import Flask, request, render_template
from flaskext.mysql import MySQL
from bd import *

# Instanciando  o Flask
app = Flask(__name__)

# Instanciando o MySQL
mysql = MySQL()

# Ligação MySQL com Flask
mysql.init_app(app)

# configurando o acesso ao MySQL:

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'escolar'

# rota para "/"
@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    # Verificando o metodo
    if request.method == 'POST':

        # Atribuindo os valores do formulario a variaveis:
        login = request.form.get('login')
        senha = request.form.get('senha')

        # Atribuindo o cursor do banco de dados a uma variavel
        cursor = mysql.get_db().cursor()

        # Obtendo o Idlogin e atribuindo ele a uma variavel
        idlogin = get_idlogin(cursor, login, senha)

        # Verificando a senha:
        if idlogin is None:
            # Retorno para a pagina do cadastro com a mensagem de erro
            return render_template('index.html', erro='Login/Senha incorretos!')
        else:
            # Obtendo o currsor para acessar o BD
            cursor = mysql.get_db().cursor()

            return render_template('oi.html', nome=login, disciplina=get_notas(cursor, idlogin))

    else:
        return render_template('index.html')




@app.route('/detalhar/<iddisciplinas>')
def detalhar(iddisciplinas):
    # Atribuindo o cursor do banco de dados a uma variavel
    cursor = mysql.get_db().cursor()
    return render_template('disciplinas.html', detalhe=get_detalhes(cursor, iddisciplinas))





# Loop de execução do app:
if __name__ == '__main__':
    app.run(debug=True)