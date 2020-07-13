import json
from udp import conexao
from udp import quebrandodados
from udp import data


def decodificar(msg):

    msg = msg[1:-1]
    msg = msg.split(";")
    with open('rastreador.json', 'r') as json_file:
        dados = json.load(json_file)


    header = msg[0]

    # Informações contidas no header, não ira utilizar todas
    """
    eventcode = header[3:5]
    statusposicao = header[39]
    """

    dados = data.datas(dados, header)
    dados["ras_eve_velocidade"] = int(header[32:35]) * 1.609344
    dados["ras_eve_direcao"] = header[35:38]
    dados["ras_eve_gps_status"] = int(header[38])
    dados["ras_eve_gprs_status"] = dados["ras_eve_gps_status"]
    dados["loc"] = [(int(header[15:23]) / 100000),(int(header[23:32]) / 100000 )]


    for i in msg[1:]:
        dados_quebrados = i.split("=")
        dados_quebrados = quebrandodados.quebrar_dados(dados_quebrados)

        #porcentagem da bateria, ainda não sei se a conta esta correta
        if dados_quebrados[0] == 'BL':
            x = 3600
            y = ((dados_quebrados[1] - x) * 100) / 700
            dados["ras_eve_porc_bat_backup"] = int(y)
        #quantidade de satelites
        elif dados_quebrados[0] == 'SV':
            dados["ras_eve_satelites"] = dados_quebrados[1]
        #passando id do aparelho pra fazer a pesquisa no banco de dados
        elif dados_quebrados[0] == 'ID':
            dados = conexao.verificar_existencia(dados,dados_quebrados[1])
            ID = dados_quebrados[1]

        #dados para quebrar e transformar em binario
        elif dados_quebrados[0] == "IO":
            dados_quebrados[1] = str(dados_quebrados[1])
            a = dados_quebrados[1][0]
            a = bin(int(a))
            dados["ras_eve_ignicao"] = int(a[2])
            b = dados_quebrados[1][1]
            b = bin(int(b))
            # +0 caso ele seja 0 o valor em dec para não dar bug na hora de inserir
            b += "0"
            dados["ras_eve_output"] = [int(b[2]),int(b[3])]
            c = dados_quebrados[1][2]
            c = bin(int(c))
            c+= "00"
            dados["ras_eve_input"] = [int(c[2]),int(c[3]),int(c[4])]

        #Tensão da entrada analógica (em milivolts) tensão
        elif dados_quebrados[0] == "AD":
            dados["ras_eve_voltagem"] = dados_quebrados[1]

    dado_e_id = [dados,ID]
    return dado_e_id
