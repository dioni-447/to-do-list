class Tarefa:
    def __init__(self, id, titulo, descricao, prazo, status="pendente"):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prazo = prazo
        self.status = status
        if not self.titulo.strip():  #busquei na IA dnv
            raise ValueError("O título da tarefa não pode ser vazio.")


tarefas=[]

def criar_tarefa(titulo, descricao, prazo):
    try:
        tarefa = Tarefa(len(tarefas) + 1, titulo, descricao, prazo)
        tarefas.append(tarefa)
        print("Tarefa criada com sucesso!")
    except ValueError as e:
        print(e)


def ver_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for tarefa in tarefas:
            print(f"\nID: {tarefa.id}, \nTítulo: {tarefa.titulo}, \nDescrição: {tarefa.descricao}, \nPrazo: {tarefa.prazo}, \nStatus: {tarefa.status}")


def deletar_tarefa(id):
    for tarefa in tarefas:
        if tarefa.id== id:
            tarefas.remove(tarefa)
            return "Tarefa deletada com sucesso!"
    return "Tarefa inexistente!"

def editar_tarefa(id):
    a=0
    for tarefa in tarefas:
        if tarefa.id == id:
            while int(a)!=9:
                print("Escolha uma opção para editar: ")
                print("1- editar título: ")
                print("2- editar descrição: ")
                print("3- editar prazo: ")
                print("4- editar status: ")
                print("9- sair")
                a=int(input())
                match a:
                    case 1:
                        tarefa.titulo=input("digite um novo titulo: ")
                    case 2:
                        tarefa.descricao=input("digite uma nova descrição: ")
                    case 3:
                        tarefa.prazo=input("digite um novo prazo: ")
                    case 4:
                        tarefa.status=input("defina o status da tarefa: ")
                    case _:
                        print("número inválido.")
            return "tarefa alterada com sucesso!"
    return "tarefa não encontrada!"


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








"""
titulo= input("Digite o título da tarefa: ")
descricao = input("Digite a descrição da tarefa: ")
prazo = input("Digite o prazo da tarefa: ")
criar_tarefa(titulo, descricao, prazo)
#ver_tarefas()
#print(deletar_tarefa(3))

print(editar_tarefa(1))
ver_tarefas()"""
