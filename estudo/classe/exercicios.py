
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depositado: R${valor:.2f}. Saldo atual: R${self.saldo:.2f}')
    
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente para saque.')
        else:
            self.saldo -= valor
            print(f'Sacado: R${valor:.2f}. Saldo atual: R${self.saldo:.2f}')

    def exibir_saldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')


conta_joao = ContaBancaria('João', 1000)

conta_joao.exibir_saldo()
conta_joao.depositar(500)
conta_joao.sacar(200)
conta_joao.exibir_saldo()



#============================================
#exercicio 2


class book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

class Library:
    def  __init__(self, name, ):
        self.name = name
        self.collection = []

    def add_book(self, book):
        self.collection.append(book)
        print(f'Book "{book.title}" by {book.author} added to the library.')

    def list_books(self):
        print(f'Books in {self.name}:')
        for book in self.collection:
            print(f'- "{book.title}" by {book.author} (Available: {"Yes" if book.available else "No"})')

    def loan_book(self, title_wanted):
        for book in self.collection:
            if book.title == title_wanted:
                if book.available:
                    book.available = False
                    print(f'Book "{book.title}" has been loaned out.')
                    return
                else:
                    print(f'Book "{book.title}" is currently not available.')
                    return
            
    def return_book(self, title_wanted):
        for book in self.collection:
            if book.title == title_wanted:
                if not book.available:
                    book.available = True
                    print(f'Book "{book.title}" has been returned.')
                    return
                else:
                    print(f'Book "{book.title}" is already available.')
                    return

# 1. Criamos a nossa biblioteca
my_library = Library('My Library')

# 2. Criamos os objetos Livro
book1 = book('1984', 'George Orwell')
book2 = book('To Kill a Mockingbird', 'Harper Lee')
book3 = book('The Great Gatsby', 'F. Scott Fitzgerald')

# 3. Adicionamos os livros na biblioteca
my_library.add_book(book1)
my_library.add_book(book2)  
my_library.add_book(book3)


# 4. Listamos o acervo inicial
my_library.list_books()

# 5. Vamos pegar um livro emprestado
my_library.loan_book('1984')

# 6. Tentando pegar o mesmo livro de novo (deve dar erro)
my_library.loan_book('1984')

# 7. Listamos novamente para ver o status atualizado
my_library.list_books()

# 8. Devolvendo o livro
my_library.return_book('1984')
