import sqlite3 as sql

conexao = sql.connect('sistema.db')
cursor = conexao.cursor()

cursor.execute('''
               CREATE TABLE pedidos (
    id INTEGER,
    cliente TEXT,
    produto TEXT,
    quantidade INTEGER,
    valor_total REAL,
    status TEXT -- 'pendente', 'enviado', 'cancelado'
    )
''');
conexao.commit()
conexao.close()