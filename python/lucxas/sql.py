import sqlite3 as sql
import os
conexao = sql.connect('sistema.db')
cursor = conexao.cursor()
"""
cursor.execute('''
    CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT,
    produto TEXT,
    quantidade INTEGER,
    valor_produto REAL,
    valor_total REAL,
    status TEXT -- 'pendente', 'enviado', 'cancelado'
    )
''');
"""
while True:
    print('escolha uma opcçao')
    print('1. novo pedido')
    print('2.atualizar pedido')
    print('3.sair')
    acao = input()
    if acao == '1':
        print('Qual o nome do cliente?')
        cliente = input()

        print('Qual o nome do produto?')
        produto = input()

        print('Qual a quantidade do produto?')
        quantidade = int(input())

        print('Qual o valor do produto?')
        valor_produto = float(input())
        
        os.system('cls')

        valor_total = quantidade * valor_produto
        status = 'pendente'


        cursor.execute('''
                INSERT INTO pedidos (cliente, produto, quantidade, valor_produto, valor_total, status)  
                VALUES (?, ?, ?, ?, ?, ?)  
        ''', (cliente, produto, quantidade, valor_produto, valor_total, status))
        conexao.commit()
    elif acao == '2':
        
        idpedido = input('qual o Id do pedido que deseja atualizar?\n')
        status_atualizados = input('\n qual o status atual? (pendente) (enviado) (cancelado) \n')
        os.system('cls')
        cursor.execute('''

               UPDATE pedidos
               SET status = ?
               WHERE id = ?    
        ''', (status_atualizados, idpedido))
        conexao.commit()
    
    elif acao == '3':
        print('saindo...')
        break
    else:
        print('essa opcao nao existe')

conexao.close()