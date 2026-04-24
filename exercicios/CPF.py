""""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""


"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import re
import random
import sys
"""
nove_numeros = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))
""" 


while True:
    cpf_enviado = input("digite seu cpf: ") \
        .replace('.', '')\
        .replace('-', '') \
        .replace(' ', '')
    cpf_enviado = re.sub(
        r'[^0-9]',
        '',
        cpf_enviado
)
    
    nove_digitos = cpf_enviado[:9]
    contador = 10
    resultado = 0
    for digito in nove_digitos:
        resultado += int(digito) * contador
        contador -= 1

    digito1 = (resultado * 10) % 11
    digito1 = digito1 if digito1 <= 9 else 0

    #segundo digito
    dez_digitos = nove_digitos + str(digito1)
    contador2 = 11
    resultado2 = 0

    for digito in dez_digitos:
        resultado2 += int(digito) * contador2
        contador2 -= 1
        
    digito2 = (resultado2 * 10) %11
    if digito2 >= 9:
        digito2 = 0
        
    cpf_gerado = f'{nove_digitos}{digito1}{digito2}'
    if cpf_enviado == cpf_gerado:
        print(f'cpf {cpf_gerado} é valido')
    else:
        print("esse cpf nao e valido")



