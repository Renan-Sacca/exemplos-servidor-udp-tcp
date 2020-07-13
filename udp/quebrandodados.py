def quebrar_dados(dados_quebrados):

    try:
        dados_quebrados[1] = int(dados_quebrados[1])
    except:
        dados_quebrados[1] = float(dados_quebrados[1])

    return dados_quebrados