# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(10, 2, 3 ,4 ,5)
print(multiplicacao)
        
    



# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

x = int(input('Digite um valor:'))

if x % 2 != 0:
    print('IMPAR')
    
else: 
    print('PAR')
    
#outra forma com funçoes

def par_impar(numero):
    return numero % 2 == 0

print(par_impar(2))
print(par_impar(5))



