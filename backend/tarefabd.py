import sqlite3

conexao=sqlite3.connect('todo_bd.db')
cursor=conexao.cursor()

cursor.execute('''
    create table if not exists tarefas(
               id integer primary key autoincrement,
               titulo text not null,
               descricao text,
               prazo datetime not null,
               status text not null default 'pendente' check (status in('pendente','ativo','completado'))
         )
    ''')
conexao.commit()
