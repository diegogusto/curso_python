
#lista de compras
import os
lista = []
while True:
    print('selecione uma opção:')
    opcao = input('[i]nserir, [a]pagar [l]listar: ')

    if opcao == "i":
        os.system('cls')
        compras = input('digite um valor: ')
        lista.append(compras)
    elif opcao == 'a':
        apagar = input("qual indice deseja apagar: ")
        
        try:
            indice = int(apagar)
            del lista[indice]
        except:
            print('nao foi possivel apagar este indice')
    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('nada pra listar')
        
        for i, compras in enumerate(lista):
            print(i, compras)
    
    else:
        print('digite i, a ou l.')

  

    