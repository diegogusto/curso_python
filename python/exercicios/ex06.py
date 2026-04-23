'''
x = input('digite um numero  inteiro: ')

if x.isdigit():
    x_int = int(x)
    par_impar = x_int % 2 == 0
    par_impar_texto = 'impar'
    
    if par_impar:
        par_impar_texto = 'par'
        
    print(f'o numero {x_int} é {par_impar_texto}')
else:
    print('Voce nao digitou um numero inteiro')
'''

"""
entrada = int(input('qual o horario atual? '))

try:
    horas = int(entrada)
    if horas <= 11 and horas >= 0 :
        print('Bom dia!')
    elif horas <= 17 and horas >= 12:
        print('Boa tarde!')
    elif horas <=23 and horas >= 18:
        print("Boa noite")
    else:
        print('digite um horario de 0-23h')
except:
    print('digite um numero inteiro')
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <=4:
        print('Seu nome é curto!')
    elif tamanho_nome <= 6: 
        print('seu nome e normal')
    else:
        print('seu nome é muito grande')
        
else:
    print('digite pelo menos uma letra.')