import json
dados = '{"nome": "Renato Lelis","profissao": "Desenvolvedor de sistemas"}'
dadosss= "{'lagitude':' 55','longitude':'66','id':'5549236','data':'15/05/2014','vel':'100'}"
dados_json = json.loads(dadosss)
print((dados_json))