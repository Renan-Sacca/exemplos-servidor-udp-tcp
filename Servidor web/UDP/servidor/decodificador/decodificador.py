import json
from udp import conexao
from udp import quebrandodados
from udp import data


def decodificar(msg):

    #Quebrando a mensagem que chega do rastreador tirando os <>
    msg = msg[1:-1]

    #Separando as mensagens por ";"
    msg = msg.split(";")

    #Abrir arquivo json padrão
    with open('../rastreador.json', 'r') as json_file:
        dados = json.load(json_file)

    #Pegando informações contidas no header da mensagem
    header = msg[0]

    #Função para pegar a data do servidor e rastreador
    dados = data.datas(dados, header)

    dados["ras_eve_velocidade"] = int(header[32:35]) * 1.609344
    dados["ras_eve_direcao"] = header[35:38]
    dados["ras_eve_gps_status"] = int(header[38])
    dados["ras_eve_gprs_status"] = dados["ras_eve_gps_status"]
    dados["loc"] = [(int(header[15:23]) / 100000),(int(header[23:32]) / 100000 )]


    for i in msg[1:]:
        #Separando nome do dado e valor por "="
        dados_quebrados = i.split("=")
        dados_quebrados = quebrandodados.quebrar_dados(dados_quebrados)

        #Porcentagem da bateria
        if dados_quebrados[0] == 'BL':
            x = 3600
            y = ((dados_quebrados[1] - x) * 100) / 700
            dados["ras_eve_porc_bat_backup"] = int(y)

        #Quantidade de satelites
        elif dados_quebrados[0] == 'SV':
            dados["ras_eve_satelites"] = dados_quebrados[1]

        #Passando id do aparelho pra fazer a pesquisa no banco de dados
        elif dados_quebrados[0] == 'ID':
            dados = conexao.verificar_existencia(dados,dados_quebrados[1])
            ID = dados_quebrados[1]

        #Dados para quebrar e transformar em binario
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

    #Retornando o arquivo json completo e o ID do aparelho para usar como resposta ACK
    dado_e_id = [dados,ID]
    return dado_e_id
