import mysql.connector
db_connection = mysql.connector.connect(host='mysql-dev.vrg.ftrack.me', user='ftrk_site', password='yh7GzoFT', database='rastreador')
cursor = db_connection.cursor()
aparelho = ''

sql= ("select a.ras_ras_id, a.ras_ras_id_aparelho,a.ras_ras_cli_id,a.ras_ras_id_indice,b.ras_vei_id_cli, b.ras_vei_id,b.ras_vei_equipamento,b.ras_vei_odometro,b.ras_vei_horimetro,c.ras_vem_id_motorista, c.ras_vem_id_veiculo from ras_rastreador a inner join ras_veiculos b on ras_ras_id_aparelho = %s and b.ras_vei_id_cli = a.ras_ras_cli_id and a.ras_ras_id = b.ras_vei_equipamento left join ras_veiculos_motorista c on b.ras_vei_id = c.ras_vem_id_veiculo")

cursor.execute(sql,(aparelho,))
for (ras_ras_id, ras_ras_id_aparelho,ras_ras_cli_id,ras_ras_id_indice,ras_vei_id_cli, ras_vei_id,ras_vei_equipamento,ras_vei_odometro,ras_vei_horimetro,ras_vem_id_motorista, ras_vem_id_veiculo) in cursor:
    dados["ras_eve_cli_id"] = ras_ras_cli_id
    dados["ras_eve_ras_id"] = ras_ras_id
    dados["ras_eve_id_indice"] = ras_ras_id_indice
    dados["ras_eve_aut_id"] = ras_vei_id
    dados["ras_eve_odometro"] = ras_vei_odometro
    dados["ras_eve_horimetro"] = ras_vei_horimetro
    dados["ras_eve_mot_id"] = ras_vem_id_motorista
