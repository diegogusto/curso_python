import os
secreta = 'augusto'
acertos = ''
tentativas = 0
while True: 
    
    tentativa = input('Digite uma letra: ')
    tentativas+= 1
    
    if len(tentativa) > 1:
        print('digite apenas uma letra')
        continue
    
    
    if tentativa in secreta:
        acertos += tentativa
    
    palavra_formada = ''
    for letra_secreta in secreta:
        if letra_secreta in acertos:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
            
    print('Palavra formada: ', palavra_formada)
        
    if palavra_formada == secreta:
        os.system('cls')
        print('PARABENS, VOCE ACERTOU')
        print('A palavra era', secreta)
        print('tentativas: ', tentativas)
        acertos = ''
        tentativa = 0
        

        
        


