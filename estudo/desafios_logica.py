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


nascimento = int(input('em que ano voce nasceu'))

