from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
import os

app = Flask(__name__)

# Definindo as variáveis de ambiente
API_BASE_URL = os.getenv("API_BASE_URL" , "http://localhost:5000/api/v1/filme")
API_DATABASE_RESET = os.getenv("API_DATABASE_RESET" , "http://localhost:5000/api/v1/database/reset") 

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para exibir o formulário de cadastro
@app.route('/inserir', methods=['GET'])
def inserir_filme_form():
    return render_template('inserir.html')

# Rota para enviar os dados do formulário de cadastro para a API
@app.route('/inserir', methods=['POST'])
def inserir_filme():
    nome = request.form['nome']
    ano_lancamento = request.form['ano_lancamento']
    categoria = request.form['categoria']

    payload = {
        'nome': nome,
        'ano_lancamento': ano_lancamento,
        'categoria': categoria
    }

    response = requests.post(f'{API_BASE_URL}/inserir', json=payload)
    
    if response.status_code == 201:
        return redirect(url_for('listar_filmes'))
    else:
        return "Erro ao inserir filme", 500

# Rota para listar todos os filmes
@app.route('/listar', methods=['GET'])
def listar_filmes():
    response = requests.get(f'{API_BASE_URL}/listar')
    filmes = response.json()
    return render_template('listar.html', filmes=filmes)

# Rota para exibir o formulário de edição de filme
@app.route('/atualizar/<int:filme_id>', methods=['GET'])
def atualizar_filme_form(filme_id):
    response = requests.get(f"{API_BASE_URL}/listar")
    #filtrando apenas o filme correspondente ao ID
    filmes = [filme for filme in response.json() if filme['id'] == filme_id]
    if len(filmes) == 0:
        return "Filme não encontrado", 404
    filme = filmes[0]
    return render_template('atualizar.html', filme=filme)

# Rota para enviar os dados do formulário de edição de filme para a API
@app.route('/atualizar/<int:filme_id>', methods=['POST'])
def atualizar_filme(filme_id):
    nome = request.form['nome']
    ano_lancamento = request.form['ano_lancamento']
    categoria = request.form['categoria']

    payload = {
        'id': filme_id,
        'nome': nome,
        'ano_lancamento': ano_lancamento,
        'categoria': categoria
    }

    response = requests.post(f"{API_BASE_URL}/atualizar", json=payload)
    
    if response.status_code == 200:
        return redirect(url_for('listar_filmes'))
    else:
        return "Erro ao atualizar filme", 500

# Rota para excluir um filme
@app.route('/excluir/<int:filme_id>', methods=['POST'])
def excluir_filme(filme_id):
    #payload = {'id': filme_id}
    payload = {'id': filme_id}

    response = requests.post(f"{API_BASE_URL}/excluir", json=payload)
    
    if response.status_code == 200  :
        return redirect(url_for('listar_filmes'))
    else:
        return "Erro ao excluir filme", 500

#Rota para resetar o database
@app.route('/reset-database', methods=['GET'])
def resetar_database():
    response = requests.delete(API_DATABASE_RESET)
    
    if response.status_code == 200  :
        return redirect(url_for('index'))
    else:
        return "Erro ao resetar o database", 500


if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')