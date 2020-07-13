from datetime import datetime
from datetime import timedelta
def datas(dados,header):

    #Pegando a data padrão que consta no rastreador para somar em semanas
    data = "06/01/1980 00:00"
    data = datetime.strptime(data, '%d/%m/%Y %H:%M')

    numesemanas = int(header[5:9])
    diasemana = int(header[9:10])
    #Horario do dia de hoje em segundos
    segundost = int(header[10:15])

    #Somando quantidade de semanas apartir de 1980
    dia_primeiro = data - timedelta(days=data.isoweekday())
    data = dia_primeiro + timedelta(weeks=numesemanas)
    data = data + timedelta(days=diasemana)

    #Convertendo o numero se segundos passados em horas do dia
    horas = segundost // 3600
    resto = segundost % 3600
    minutos = resto // 60
    segundos = resto % 60

    #Somando horario com a data
    data = data + timedelta(hours=horas, minutes=minutos, seconds=segundos)
    #Convertendo para timestamp
    dia_ras = datetime.timestamp(data)
    #Pegando data do servidor e convertendo para timestamp
    dia_servidor = datetime.now()
    dia_servidor = datetime.timestamp(dia_servidor)

    #Colocando dados obtidos do json
    dados["ras_eve_data_gps"] = dia_ras
    dados["ras_eve_data_enviado"] = dia_ras
    dados["ras_eve_data_servidor"] = dia_servidor

    return dados



