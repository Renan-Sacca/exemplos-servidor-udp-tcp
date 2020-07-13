import json
"""dados = {"name": "Madame Uppercut",
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
"""
dicionario = {
    "ras_eve_id_indice" : None,
    "ras_eve_cli_id" : None,
    "ras_eve_aut_id" : None,
    "ras_eve_mot_id" : None,
    "ras_eve_ras_id" : None,
    "ras_eve_odometro" : None,
    "ras_eve_horimetro" : None,
    "ras_eve_porc_bat_backup" : None,
    "ras_eve_direcao" : None,
    "ras_eve_satelites" : None,
    "ras_eve_ignicao" : None,
    "ras_eve_gps_status" : None,
    "ras_eve_gprs_status" : None,
    "ras_eve_validade" : None,
    "ras_eve_data_gps" : None,
    "ras_eve_data_enviado" : None,
    "ras_eve_data_servidor" : None,
    "ras_eve_velocidade" : None,
    "ras_eve_voltagem" : None,
    "ras_eve_voltagem_backup" : None,
    "ras_eve_alertas" : None,
    "ras_eve_input" : None,
    "ras_eve_output" : None,
    "loc" : None
}

with open('../../udp/rastreador.json', 'w') as json_file:
    json.dump(dicionario, json_file, indent=4)