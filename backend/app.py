from flask import Flask, jsonify, g, request
import tarefabd, sqlite3

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('todo_bd.db')
        g.db.row_factory = sqlite3.Row  # pesquisa o que isso faz!
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route("/")#definir rota principal
def home():
    db = get_db()
    return "Olá, Flask!"


@app.route("/tarefas", methods=['GET'])
def ver_tarefas():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('select * from tarefas')
    dados = cursor.fetchall()
    tarefas = []
    for linha in dados:
        tarefas.append({
            "id": linha[0],
            "titulo": linha[1],
            "descricao": linha[2],
            "prazo": linha[3],
            "status": linha[4]
        })
    return jsonify(itens=tarefas), 200

@app.route("/tarefas", methods=["POST"])
def criar_tarefas():
    db = get_db()
    cursor = db.cursor()
    dados = request.get_json()
    titulo=dados.get('titulo')
    descricao=dados.get('descricao')
    prazo=dados.get('prazo')
    if not titulo:
        return jsonify({"erro": "título é obrigatório"}), 400

    cursor.execute('insert into tarefas (titulo, descricao, prazo) values (?,?,?)',(titulo,descricao,prazo))
    db.commit()
    return "tarefa criada com sucesso",201

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def deletar_tarefas(id):
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute('delete from tarefas where id=?',(id,))
        if cursor.rowcount==0:
            return("\nID não encontrado\n"),404
        else:
            db.commit()
            return jsonify({"mensagem": "Tarefa deletada com sucesso"}),200
    except sqlite3.Error as e:
        return(e),400

@app.route("/tarefas/<int:id>", methods=['PUT'])
def editar_tarefas(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('select id from tarefas where id=?',(id,))
    if cursor.fetchone() is None:
        return jsonify({"mensagem": "Tarefa não encontrada"}),404
    else:
        dados = request.get_json()
        try:
            titulo=dados.get('titulo')
            if titulo is not None:
                cursor.execute('update tarefas set titulo=? where id=?',(titulo,id))
            descricao=dados.get('descricao')
            if descricao is not None:
                cursor.execute('update tarefas set descricao=? where id=?',(descricao,id))
            prazo=dados.get('prazo')
            if prazo is not None:
                cursor.execute('update tarefas set prazo=? where id=?',(prazo,id))
            status=dados.get('status')
            if status is not None:
                cursor.execute('update tarefas set status=? where id=?',(status,id))
            db.commit()
            return jsonify({'mensagem':"Tarefa atualizada com sucesso"}),200
        except sqlite3.Error:
            return jsonify({"mensagem":"Erro"}),400


if __name__ == "__main__":#modo de depuração, não entendi mt bem mas parece ser essencial
    app.run(debug=True)