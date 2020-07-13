import json
dados = {"name": "Madame Uppercut",
        "age": 39,
        "secretIdentity": "Jane Wilson",
        "powers": [
        "Million tonne punch",
        "Damage resistance",
         "Superhuman reflexes"]}

dadoss = {
    'nome': 'Renato Lelis',
    'profissao': 'Desenvolvedor de sistemas'
}
dados_json = json.dumps(dadoss)
print((dados_json))

with open('dadoss.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4)