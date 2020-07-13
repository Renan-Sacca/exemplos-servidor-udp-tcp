import json
with open('dadoss.json', 'r') as json_file:
    dados = json.load(json_file)



    
print(dados)
print(type(dados))