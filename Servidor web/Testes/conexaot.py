import mysql.connector
import json

db_connection = mysql.connector.connect(host='mysql-dev.vrg.ftrack.me', user='ftrk_site', password='yh7GzoFT', database='rastreador')
cursor = db_connection.cursor()
aparelho = '304691'

sql = ("SELECT ras_ras_id,ras_ras_id_aparelho,ras_ras_cli_id,ras_ras_id_indice FROM ras_rastreador WHERE ras_ras_id_aparelho = %s".format(aparelho))
cursor.execute(sql,(aparelho,))

for (ras_ras_id,ras_ras_id_aparelho, ras_ras_cli_id,ras_ras_id_indice) in cursor:
    print(ras_ras_id,ras_ras_id_aparelho, ras_ras_cli_id,ras_ras_id_indice)

sql = ("select ras_vei_id_cli, ras_vei_id,ras_vei_equipamento,ras_vei_odometro,ras_vei_horimetro from ras_veiculos where ras_vei_id_cli = %s and ras_vei_equipamento = %s")

cursor.execute(sql,(ras_ras_cli_id,ras_ras_id,))

    #pegando dados na tabela veiculos
for (ras_vei_id_cli, ras_vei_id,ras_vei_equipamento,ras_vei_odometro,ras_vei_horimetro) in cursor:
    print(ras_vei_id_cli, ras_vei_id,ras_vei_equipamento,ras_vei_odometro,ras_vei_horimetro)

sql("select a.ras_ras_id, a.ras_ras_id_aparelho,a.ras_ras_cli_id,a.ras_ras_id_indice,"
    "b.ras_vei_id_cli, b.ras_vei_id,b.ras_vei_equipamento,b.ras_vei_odometro,b.ras_vei_horimetro,"
    "c.ras_vem_id_motorista, c.ras_vem_id_veiculo"
    "from ras_rastreador a inner join ras_veiculos b "
    "on ras_ras_id_aparelho = %s"
    " and b.ras_vei_id_cli = a.ras_ras_cli_id "
    "and a.ras_ras_id = b.ras_vei_equipamento left join ras_veiculos_motorista c"
    "on b.ras_vei_id = c.ras_vem_id_veiculo")

cursor.execute(sql,(aparelho,))
for (ras_ras_id, ras_ras_id_aparelho,ras_ras_cli_id,ras_ras_id_indice,ras_vei_id_cli, ras_vei_id,ras_vei_equipamento,ras_vei_odometro,ras_vei_horimetro,ras_vem_id_motorista, ras_vem_id_veiculo) in cursor:
    print(ras_ras_id, ras_ras_id_aparelho,ras_ras_cli_id,ras_ras_id_indice,ras_vei_id_cli, ras_vei_id,ras_vei_equipamento,ras_vei_odometro,ras_vei_horimetro,ras_vem_id_motorista, ras_vem_id_veiculo)



