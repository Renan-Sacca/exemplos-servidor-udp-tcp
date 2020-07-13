import redis

def banco_redis(dados,aparelho):

    aparelho = str(aparelho)
    # Conexão redis
    r = redis.Redis(host="localhost", port=6379)
    #Pesquisa para ver se existe dados ja no redis
    s = r.hget("aparelho:{}".format(aparelho), "id_aparelho")

    # caso não exista, pegar dados do mysql e colocar no json e redis
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



