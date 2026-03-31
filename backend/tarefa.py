import tarefabd,sqlite3

conexao=tarefabd.conexao
cursor=tarefabd.cursor

class Tarefa:
    def __init__(self, id, titulo, descricao, prazo, status="pendente"):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prazo = prazo
        self.status = status
        if not self.titulo.strip(): 
            raise ValueError("O título da tarefa não pode ser vazio.")


def criar_tarefa(titulo, descricao, prazo):
    try:
        cursor.execute('''
            insert into tarefas (titulo, descricao, prazo) values(?,?,?)''',(titulo, descricao, prazo))
        conexao.commit()
        print("\n\nTarefa criada com sucesso!\n\n")
    except sqlite3.Error as e:
        print(e)


def ver_tarefas():
    cursor.execute('select * from tarefas')
    tarefas=cursor.fetchall()
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for linha in tarefas:
            print(f"\nID: {linha[0]}, \nTítulo: {linha[1]}, \nDescrição: {linha[2]}, \nPrazo: {linha[3]}, \nStatus: {linha[4]}\n\n")


def deletar_tarefa(id):
    try:
        cursor.execute('delete from tarefas where id=?',(id,))
        if cursor.rowcount==0:
            print("\nID não encontrado\n")
        else:
            print('\nTarefa deletada com sucesso.\n')
            conexao.commit()
    except sqlite3.Error as e:
        print(e)
        


def editar_tarefa(id):
    a=0
    cursor.execute('select id from tarefas where id=?',(id,))
    if cursor.fetchone() is None:
        print('\nTarefa não encontrada\n')
    else:
        while int(a)!=9:
            print("\nEscolha uma opção para editar: ")
            print("1- editar título: ")
            print("2- editar descrição: ")
            print("3- editar prazo: ")
            print("4- editar status: ")
            print("9- sair")
            a=int(input())
            match a:
                case 1:
                    titulo=input("digite um novo titulo: ")
                    cursor.execute('update tarefas set titulo=? where id=?',(titulo,id,))
                    conexao.commit()
                case 2:
                    descricao=input("digite uma nova descrição: ")
                    cursor.execute('update tarefas set descricao=? where id=?',(descricao,id,))
                    conexao.commit()
                case 3:
                    prazo=input("digite um novo prazo: ")
                    cursor.execute('update tarefas set prazo=? where id=?',(prazo,id,))
                    conexao.commit()
                case 4:
                    status = ''
                    while status not in ['pendente','ativo','completado']:
                        status=input("defina o status da tarefa: ")
                        if status not in ['pendente','ativo','completado']:
                            print("status inválido!")
                    cursor.execute('update tarefas set status=? where id=?',(status,id,))
                    conexao.commit()
                case _:
                    print("número inválido.")
        conexao.commit()
        return "tarefa alterada com sucesso!"


while True:
    print("Escolha um número: ")
    print("1- criar tarefa: ")
    print("2- ver tarefas criadas: ")
    print("3- editar tarefas: ")
    print("4- deletar tarefas: ")
    print("9- sair")
    a=int(input())
    match a:
        case 1:
            print("\n\n")
            titulo= input("Digite o título da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            prazo = input("Digite o prazo da tarefa: ")
            criar_tarefa(titulo, descricao, prazo)
        case 2:
            ver_tarefas()
        case 3:
            i=int(input("Digite o id da tarefa: "))
            print(editar_tarefa(i))
        case 4:
            i=int(input("Digite o id da tarefa: "))
            print(deletar_tarefa(i))
        case 9:
            if a==9:
                break
        case _:
            print("número inválido.")

