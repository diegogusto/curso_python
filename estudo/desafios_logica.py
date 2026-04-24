"""""
print('Digite 3 notas:')
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = 0
soma_notas = 0

soma_notas = (nota1 + nota2 + nota3) / 3

if soma_notas >= 7:
    print("Aprovado")
else:
    print("reprovado")
"""

"""
for i in range(1, 11):
    print(i)
"""
soma_positivos = 0


valor = int(input('digite um numero: '))
soma_positivos += valor
while valor != 0:
    valor = int(input('digite um numero: '))
    if valor > 0:
        soma_positivos += valor

print(soma_positivos)
    