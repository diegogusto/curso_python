"""calculadora  com  while"""

while True:
    n1 = input('Digite um numero:')
    n2 = input('Digite outro numero:')
    operador = input('Digite um operador(+ - / *)')
    
    numeros_validos = None
    n1_float = 0
    n2_float = 0
    
    try:
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print("Um dos numeros sao invalidos")
        continue
    
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador invalido')
        
    if len(operador) > 1:
        print('digite apenas um operador')
        continue
    
    print('realizando o calculo. confira o resultado abaixo:')
    
    if operador == '+':
        print(n1_float + n2_float)
    elif operador == '-':
        print(n1_float - n2_float)
    elif operador == '*':
        print(n1_float * n2_float)
    elif operador == '/':
        print(n1_float / n2_float)
    else:
        print('och tropa')
    
    
    
    
    
    
    sair = input('quer sair? sim?').lower().startswith('s')
    print(sair)
    
    if sair is True:
        break