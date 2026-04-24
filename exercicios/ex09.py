frase = 'O python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'python foi criado por guido van rossum.'.upper()
    
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
