def quebrar_dados(dados_quebrados):
    #Tenta transformar o numero em inteiro, caso seja um numero quebrado ele transforma em float
    try:
        dados_quebrados[1] = int(dados_quebrados[1])
    except:
        dados_quebrados[1] = float(dados_quebrados[1])

    return dados_quebrados