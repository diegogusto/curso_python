# "Banco de dados" simples
usuarios = {
    "diego": "1234",
    "ana": "abcd"
}

usuario_logado = None


# 🔐 Decorador de autenticação
def precisa_login(func):
    def interna(*args, **kwargs):
        if not usuario_logado:
            print("❌ Você precisa fazer login!")
            return
        return func(*args, **kwargs)
    return interna


# 📊 Decorador de log
def log(func):
    def interna(*args, **kwargs):
        print(f"[LOG] {usuario_logado} executou {func.__name__}")
        return func(*args, **kwargs)
    return interna


# 🔑 Login
def login():
    global usuario_logado

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario in usuarios and usuarios[usuario] == senha:
        usuario_logado = usuario
        print(f"✅ {usuario} logado com sucesso!")
    else:
        print("❌ Usuário ou senha inválidos")


# 🚪 Logout
def logout():
    global usuario_logado

    if usuario_logado:
        print(f"👋 {usuario_logado} saiu")
        usuario_logado = None
    else:
        print("⚠️ Ninguém está logado")


# 🔒 Funções protegidas

@log
@precisa_login
def ver_dados():
    print("📊 Dados secretos do sistema")


@log
@precisa_login
def alterar_senha():
    global usuarios
    nova_senha = input("Nova senha: ")
    usuarios[usuario_logado] = nova_senha
    print("🔑 Senha alterada com sucesso")


# 🧠 Menu principal
def menu():
    while True:
        print("\n=== SISTEMA ===")
        print("1 - Login")
        print("2 - Ver dados")
        print("3 - Alterar senha")
        print("4 - Logout")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            login()
        elif opcao == "2":
            ver_dados()
        elif opcao == "3":
            alterar_senha()
        elif opcao == "4":
            logout()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("❌ Opção inválida")


# ▶️ Executar sistema
menu()
    