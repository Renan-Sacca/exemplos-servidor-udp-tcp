import mysql.connector
def conectar(dados,aparelho):
    aparelho = str(aparelho)
    db_connection = mysql.connector.connect(host='mysql-dev.vrg.ftrack.me', user='ftrk_site', password='yh7GzoFT', database='rastreador')
    cursor = db_connection.cursor()

    sql = ("SELECT ras_ras_id,ras_ras_id_aparelho,ras_ras_cli_id,ras_ras_id_indice FROM ras_rastreador WHERE ras_ras_id_aparelho = %s")
    cursor.execute(sql,(aparelho,))


    #pegando dados na tabela de rastreador
    for (ras_ras_id,ras_ras_id_aparelho, ras_ras_cli_id,ras_ras_id_indice) in cursor:
        if ras_ras_id_aparelho == aparelho:
            dados["ras_eve_cli_id"] = ras_ras_cli_id
            dados["ras_eve_ras_id"] = ras_ras_id
            dados["ras_eve_id_indice"] = ras_ras_id_indice
            print(ras_ras_id,ras_ras_id_aparelho, ras_ras_cli_id,ras_ras_id_indice)


    sql = ("SELECT ras_vei_id_cli, ras_vei_id,ras_vei_equipamento,ras_vei_odometro,ras_vei_horimetro FROM ras_veiculos")
    cursor.execute(sql)

    #pegando dados na tabela veiculos
    for (ras_vei_id_cli, ras_vei_id,ras_vei_equipamento,ras_vei_odometro,ras_vei_horimetro) in cursor:
        if dados["ras_eve_cli_id"] == ras_vei_id_cli and dados["ras_eve_ras_id"] == ras_vei_equipamento:
            dados["ras_eve_aut_id"] = ras_vei_id
            dados["ras_eve_odometro"] = ras_vei_odometro
            dados["ras_eve_horimetro"] = ras_vei_horimetro
            print(ras_vei_id_cli, ras_vei_id,ras_vei_equipamento,ras_vei_odometro,ras_vei_horimetro)

    sql = ("SELECT ras_vem_id_motorista, ras_vem_id_veiculo FROM ras_veiculos_motorista")
    cursor.execute(sql)

    #ID DO MOTORISTA DEFALT CASO NÂO EXISTA NA TABELA VEICULOS/MOTORISTAS
    dados["ras_eve_mot_id"] = 9999
    for (ras_vem_id_motorista, ras_vem_id_veiculo) in cursor:
        if dados["ras_eve_aut_id"] == ras_vem_id_veiculo:
            dados["ras_eve_mot_id"] = ras_vem_id_motorista

    cursor.close()
    return dados



