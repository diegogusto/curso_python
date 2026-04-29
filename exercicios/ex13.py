# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
print(duplicar(2))
print(triplicar(3))


#------------------------------------------

def criar_soma(soma):
    def somar(numero):
        return numero + soma
    return somar

somar1 = criar_soma(2)
somar2 = criar_soma(10)
print(somar1(2))
print(somar2(5))