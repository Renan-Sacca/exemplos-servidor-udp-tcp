import mysql.connector
import redis

def verificar_existencia(dados,aparelho):
    aparelho = str(aparelho)
    r = redis.Redis(host="localhost", port=6379)
    s = r.hget("aparelho:{}".format(aparelho), "id_aparelho")
    if s == None:
        dados = banco_mysql(dados, aparelho)
        return dados
    else:
        dados["ras_eve_cli_id"] = r.hget("aparelho:{}".format(aparelho), "ras_ras_cli_id").decode()
        dados["ras_eve_ras_id"] = r.hget("aparelho:{}".format(aparelho), "ras_ras_id").decode()
        dados["ras_eve_id_indice"] = r.hget("aparelho:{}".format(aparelho), "ras_ras_id_indice").decode()
        dados["ras_eve_aut_id"] = r.hget("aparelho:{}".format(aparelho), "ras_vei_id").decode()
        dados["ras_eve_mot_id"] = r.hget("aparelho:{}".format(aparelho), "ras_vei_id_mot").decode()
        return dados

def banco_mysql(dados,aparelho):
    db_connection = mysql.connector.connect(host='', user='', password='', database='')
    cursor = db_connection.cursor()
    r = redis.Redis(host="localhost", port=6379)

    sql = ("""SELECT ras_ras_id,ras_ras_id_aparelho,ras_ras_cli_id,ras_ras_id_indice,
                ras_ins_id_rastreador,ras_ins_id_veiculo,ras_ins_instalado,
                ras_vei_id_cli,ras_vei_id,ras_vei_id_mot
                FROM ras_rastreador
                INNER JOIN ras_instalacao 
                ON ras_ras_id = ras_ins_id_rastreador
                INNER JOIN ras_veiculos 
                ON ras_ins_id_veiculo = ras_vei_id
                WHERE ras_ras_id_aparelho = %s 
                AND ras_ins_instalado = 2;""")


    cursor.execute(sql, (aparelho,))
    for (ras_ras_id,ras_ras_id_aparelho,ras_ras_cli_id,ras_ras_id_indice,
                ras_ins_id_rastreador,ras_ins_id_veiculo,ras_ins_instalado,
                ras_vei_id_cli,ras_vei_id,ras_vei_id_mot) in cursor:
        dados["ras_eve_cli_id"] = ras_ras_cli_id
        dados["ras_eve_ras_id"] = ras_ras_id
        dados["ras_eve_id_indice"] = ras_ras_id_indice
        dados["ras_eve_aut_id"] = ras_vei_id
        dados["ras_eve_mot_id"] = ras_vei_id_mot

        r.hset("aparelho:{}".format(aparelho), "id_aparelho",aparelho)
        r.hset("aparelho:{}".format(aparelho), "ras_ras_cli_id", ras_ras_cli_id)
        r.hset("aparelho:{}".format(aparelho), "ras_ras_id", ras_ras_id)
        r.hset("aparelho:{}".format(aparelho), "ras_ras_id_indice", ras_ras_id_indice)
        r.hset("aparelho:{}".format(aparelho), "ras_vei_id", ras_vei_id)
        r.hset("aparelho:{}".format(aparelho), "ras_vei_id_mot", ras_vei_id_mot)

        #dados["ras_eve_odometro"] = ras_vei_odometro
        #dados["ras_eve_horimetro"] = ras_vei_horimetro
        #if ras_vem_id_motorista == None:
         #   dados["ras_eve_mot_id"] = ras_vei_id_mot
        #else:
         #   dados["ras_eve_mot_id"] = ras_vem_id_motorista

    cursor.close()
    return dados





