usuarios = {
    'diego': "1234",
    'ana': "abcd",
}

usuario_logado = None

#decorador de autentificação

def login():
    global usuario_logado
    
    usuario = input('Usuario: ')
    senha = input("Senha: ")
    
    if usuario in usuarios and usuarios[usuario] == senha:
        usuario_logado = usuario
        print(f"{usuario} logado com sucesso")
    else:
        print(f'usuario ou senha invalidos')
        
    