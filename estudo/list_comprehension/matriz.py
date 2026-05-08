#forma normal de fazer uma matriz:

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
        
#com list:
lista = [(x,y) for x in range(3)  for y in range(3)]

print(lista)