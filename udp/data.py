
from datetime import datetime
from datetime import timedelta
def datas(dados,header):
    data = "06/01/1980 00:00"
    data = datetime.strptime(data, '%d/%m/%Y %H:%M')
    numesemanas = int(header[5:9])
    diasemana = int(header[9:10])
    #horariododiadehjemsegundos
    segundost = int(header[10:15])

    dia_primeiro = data - timedelta(days=data.isoweekday())
    data = dia_primeiro + timedelta(weeks=numesemanas)
    data = data + timedelta(days=diasemana)

    horas = segundost // 3600
    resto = segundost % 3600
    minutos = resto // 60
    segundos = resto % 60

    data = data + timedelta(hours=horas, minutes=minutos, seconds=segundos)
    dia_ras = datetime.timestamp(data)
    dia_servidor = datetime.now()
    dia_servidor = datetime.timestamp(dia_servidor)
    dados["ras_eve_data_gps"] = dia_ras
    dados["ras_eve_data_enviado"] = dia_ras
    dados["ras_eve_data_servidor"] = dia_servidor

    return dados



