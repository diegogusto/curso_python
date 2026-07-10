#triplicar uma lista usando map
produtos = [
    {"nome": "camisa", "preco": 50},
    {"nome": "calça", "preco": 100},
    {"nome": "sapato", "preco": 150},
]

novo_produtos = list(map(lambda p: { "preco": p["preco"] * 3}, produtos))
print(produtos)
print()
print(novo_produtos)


#valor total dos produtos:
total = 0
for p in produtos:
    total += p["preco"]

print(total)
