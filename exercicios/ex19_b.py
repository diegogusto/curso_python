
import json
from ex19 import CAMINHO_ARQUIVO, person

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    persons = json.load(arquivo)
    p1 = person(**persons[0])
    p2 = person(**persons[1])
    p3 = person(**persons[2])
   
    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)
