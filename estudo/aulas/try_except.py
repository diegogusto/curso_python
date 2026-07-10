# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')
    
    
    
    
#forma correta de se usar:
try:
    numero = int(input("Digite um número: "))
    print(10 / numero)
except ValueError:
    print("Você precisa digitar um número válido!")
except ZeroDivisionError:
    print("Não pode dividir por zero!")