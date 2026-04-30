
# Exercício - sistema de perguntas e respostas
#meu jeito: 

"""
pergunta = input("Pergunta: Quanto é 2+2?
Opções:
a) 1
b) 3
c) 4
d) 5
Escolha uma opção:)

if pergunta.lower() == 'c':
    print("Acertou✅")
else:
    print("errou❌")

pergunta2 = input(Pergunta: Quanto é 5*5?
Opções:
a) 25
b) 55
c) 10
d) 51
Escolha uma opção: )

if pergunta2.lower() == 'a':
    print("Acertou✅")
else:
    print("Errou❌")

pergunta3 = input(Pergunta: Quanto é 10/2?
Opções:
a) 4
b) 5
c) 2
d) 1
Escolha uma opção: )

if pergunta3.lower() == 'b':
    print("Acertou✅")
else:
    print("Errou❌")
"""

#jeito melhor:
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')   
    
    
    
