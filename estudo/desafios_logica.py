"""""
print('Digite 3 notas:')
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = 0
soma_notas = 0

soma_notas = (nota1 + nota2 + nota3) / 3

if soma_notas >= 7:
    print("Aprovado")
else:
    print("reprovado")
"""

"""
for i in range(1, 11):
    print(i)
"""


"""
soma_positivos = 0


valor = int(input('digite um numero: '))
soma_positivos += valor
while valor != 0:
    valor = int(input('digite um numero: '))
    if valor > 0:
        soma_positivos += valor

print(soma_positivos)
"""


"""
print('digite tres numeros:')
a = int(input())
b = int(input())
c = int(input())

soma = a + b

if soma < c:
    print(f'a soma dos dois primeiros valores é menor que o ultimo ({soma})')
else:
    print(f'a soma dos dois primeiros valores é maior que o ultimo ({soma})')
"""

"""
print('digite dois valores')
a = int(input())
b = int(input())

if a == b:
    c = a + b
else:
    c = a * b

print(c)
"""

"""
x = int(input("digite um valor"))

print(x - 1)
print(x + 1)
"""

"""
valor = float(input("digite um numero"))

porcentagem = valor * 0.05
reajuste =  valor - porcentagem

print(reajuste)
"""
    
"""   
print('digite 3 valores:')
a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    maior = a
    if b > c:
        meio = b
        fim = c
    else:
        meio = c
        fim = b
elif b > a and b > c:
    maior = b
    if a > c:
        meio = a
        fim = c
    else:
        meio = c
        fim = a    
else:
    maior = c
    if a > b:
        meio = a
        fim = b
    else:
        meio = b
        fim = a

print(maior, meio, fim)

#forma direta:

valores = [a, b, c]
valores.sort(reverse=True)

print(valores)

"""

"""
peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}. Você está abaixo do peso")

elif imc < 25:
    print(f"Seu IMC é {imc:.2f}. Você está com peso ideal")

elif imc < 30:
    print(f"Seu IMC é {imc:.2f}. Você está com sobrepeso")

elif imc < 35:
    print(f"Seu IMC é {imc:.2f}. Você está com obesidade grau 1")

elif imc < 40:
    print(f"Seu IMC é {imc:.2f}. Você está com obesidade grau 2")

else:
    print(f"Seu IMC é {imc:.2f}. Você está com obesidade grau 3")
    
"""

"""
nome = input('escreva seu nome: ')

nota1 = float(input('digite a primeira nota'))
nota2 = float(input('digite a segunda nota'))
nota3 = float(input('digite a terceira nota'))
nota4 = float(input('digite a quarta nota'))

soma = nota1 + nota2 + nota3 + nota4
media = soma / 4

print(media)
if media >= 7.0:
    print(f'parabens {nome}, voce foi aprovado')
    
else:
    print(f'voce reprovou {nome}, tente novamente!')

"""

"""
valor_produto = float(input("digite o valor do produto"))
forma_pagamento = input(
    "Qual a forma de pagamento: \
    Dinheiro[DIN]\
    Cartao de credito a vista[C] \
    Parcelado em 2x[2x] \
    Parcelado em 3x ou mais[3x+]"
)

if forma_pagamento == "DIN":
    porcentagem = valor_produto / 0.15
    valor_pagar = valor_produto - porcentagem
    print(f'sua forma de pagamento foi em dinheiro, e o valor total foi de {valor_pagar}')

elif forma_pagamento == "C":
    porcentagem = valor_produto / 0.10
    valor_pagar = valor_produto - porcentagem
    print(f'sua forma de pagamento foi em cartao a vista, e o valor total foi de {valor_pagar}')

elif forma_pagamento == "2x":
    print(f'sua forma de pagamento foi em cartao 3x, e o valor total foi de {valor_produto}')
    
elif forma_pagamento == "3x":
    porcentagem = valor_produto / 0.10
    valor_pagar = valor_produto + porcentagem
    print(f'sua forma de pagamento foi em cartao 3x, e o valor total foi de {valor_pagar}')

else:
    print('porfavor, digite apenas as tags entre cochetes')


"""

"""
print('digite dois valores')
a = input()
b = input()

mudanca = a
a = b
b = mudanca

print(a, b)

"""


"""
from datetime import datetime 

ano_nascimento = int(input("digite o ano de nascimento:"))

ano_atual = datetime.now().year

anos = ano_atual - ano_nascimento

total_dias = anos * 365

anos_finais = total_dias // 365
resto = total_dias % 365

meses = resto // 30
dias = resto % 30

print(anos_finais, meses, dias)

"""


"""
anos = 0
francisco = 1.50
sara = 1.10

while sara < francisco:
    anos += 1
    sara += 0.03
    francisco += 0.02

print(francisco, sara, anos)

"""
    
"""
x = int(input())

for multi in range(1,11):
    resultado = x * multi
    print(resultado)

"""

"""
print('digite as seguintes informações:')

valor_hora = float(input('valor da hora aula'))
horas_dia = float(input('quantas horas por dia'))
aulas_mes = int(input('numero de aulas no mes'))

persentual_inss = 0.92

salario = valor_hora * (horas_dia * aulas_mes) * persentual_inss

print(salario)
"""
"""
frase = 'eu sou gay porra'.upper()
    
i = 0
apareceu_mais = 0
letra_mais = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
    
    quanti_letra = frase.count(letra_atual)
    
    if apareceu_mais < quanti_letra:
        apareceu_mais = quanti_letra
        letra_mais = letra_atual
    
    i += 1
    
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_mais}" que apareceu '
    f'{apareceu_mais}x'
)


textoo = input('digite seu texto')
lista = []
def primeiro_unico(texto):
    for i in texto:
        lista.append(i)
        if i in lista:
            print(i)
            
print(primeiro_unico(textoo))

"""

"""
parar = ''
print('digite seu calculo, digite "00", para calcular')
while valores1 or valores2 != '=':
    valores1 = int(input('primeiro valor'))
    valores2 = int(input('segundo valor'))
    print('qual operador vai ser utilizado?')
    operadores = input()
    
    if operadores == '+':
        resultado = valores1 + valores2
    elif operadores == '-':
        resultado = valores1 - valores2
    elif operadores == '*':
        resultado = valores1 * valores2
    elif operadores == '/':
        resultado = valores1 / valores2
    
"""


"""
alunos = []
while True:
    nome = input('digite seu nome: ')
    if nome == 'sair':
        break
    
    nota = float(input('digite sua  nota:'))
    
    aluno = {
        'nome': nome,
        'nota': nota
    }
    
    alunos.append(aluno)
    
#mostrar resultado:
    for aluno in alunos:
        print(aluno['nome'], aluno['nota'])
        
"""



"""
usuario = 'diego'
senha = 2707

for tentativas in range(3):
    print('digite usuario e senha abaixo:')
    usuario_tentativa = input('usuario: ')
    senha_tentativa = int(input('Senha: '))
    
    if usuario_tentativa == usuario:
        if senha_tentativa == senha:
            print('parabens voce acertou')      
            break
        else:
            print('Voce digitou a senha errada!')
    else:
        print('voce digitou o usuario errado!')
          
"""


