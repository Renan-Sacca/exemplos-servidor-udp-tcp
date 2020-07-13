import json
dados = [0] * 2
dados[0] = '{"nome": "Renato Lelis","profissao": "Desenvolvedor de sistemas"}'
dados[1] = '{"nome": "renan","profissao": "dante"}'
dados_json = [0] * 2
dados_json[0] = json.loads(dados[0])
dados_json[1] = json.loads(dados[1])
print(dados_json)
print((dados_json[0]["nome"]))
print((dados_json[1]["profissao"]))
