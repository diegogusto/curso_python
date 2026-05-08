
"""
def saudar(nome):
    print(f'olá, {nome}!')
    
print(saudar('diego'))
"""

"""
def soma(a, b):
    return a + b

resultado = soma(5,3)
print(resultado)
"""


"""
def par_ou_impar(numero):
    if numero %2 == 0:
        return 'par'
    else:
        return 'impar'
    
resultado = par_ou_impar(5)
print(resultado)
"""

"""
def maior(a, b):
    if a > b:
        return a
    else:
        return b
    
maior_menor = maior(1,2)
print(maior_menor)

"""

"""
def media(n1, n2, n3):
    print((n1 + n2 + n3) /3)
    
    
print(media(2, 2, 2))

"""

"""
def calculadora(a, b, operacao):
    if operacao == '+':
        return a + b
    elif operacao == '-':
        return a - b
    elif operacao == '*':
        return a * b
    elif operacao == '/':
        return a / b
    else:
        return "operacao invalida"
    
print(calculadora(2, 2, "/"))

"""

"""
def contar(inicio, fim):
    for i in range(inicio, fim +1):
        print(i)
        
print(contar(2, 6))

"""

"""
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
        
print(fatorial(5))
"""



"""
def maior_lista(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior =  numero
    return maior

print(maior_lista([2, 5, 6, 10, 2, 8]))

"""

"""
def avaliar_nota(nota):
    if nota < 0 or nota > 10:
        return 'nota invalida'
    elif nota >= 7:
        return 'aprovado'
    elif nota >= 5:
        return 'recuperacao'
    else: 
        return 'reprovado'
    
nota_pessoal = int(input())
print(avaliar_nota(nota_pessoal))

"""

"""
def dobro_lista(lista):
    nova_lista = []
    for  numero in lista:
        nova_lista.append(numero * 2)
    return nova_lista

print(dobro_lista([2, 4, 6]))
"""