from flask import Flask, request, jsonify

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Pai Rico 1',
        'Autor': 'Roberto'
    },
    {
        'id': 2,
        'título': 'Pai Rico 2',
        'Autor': 'Roberto 2'
    },
    {
        'id': 3,
        'título': 'Pai Rico 3',
        'Autor': 'Roberto 3'
    }
]

# Criar um novo livro
@app.route('/livros', methods=['POST'])
def incluir_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


#Obtendo todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Obtendo livro por id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Alterando um livro        
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def exluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

            return jsonify(livros)



app.run(port=5000, host='localhost', debug=True)