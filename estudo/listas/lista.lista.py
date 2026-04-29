#lista de listas e seus indices

salas = [
    ["maria", 'helena',],
    ['elaine',],
    ['luiz', 'joao', 'eduarda', (0, 10, 20, 30, 40)],
]

print(salas[2][2])
print(salas[0][0])
print(salas[1][0])
print(salas[2][3][3])
print(salas[2][3][2])

for sala in salas:
    print(f'a sala é {sala}')
    for aluno in sala:
        print(aluno)