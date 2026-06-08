# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = 'exercicios/ex19_tasks.json'

class person:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = person('João', 30)
p2 = person('Maria', 22)
p3 = person('Pedro', 35)
bd = [vars(p1), vars(p2), vars(p3)]

with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
