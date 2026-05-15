"""
def decorador(func):
    def interna():
        print('antes...')
        func()
        print('depois')
    return interna

@decorador
def saudacao():
    print('ola')
    
saudacao()
"""
nome = ""
def decorador(func):
    def interna(*args, **kwargs):
        print(f"chamando funcao {func.__name__} com argumentos {args}")
        func(*args, **kwargs)
    return interna

@decorador
def saudacao(nome):
    print(f"ola, {nome}")
    
saudacao('diego')