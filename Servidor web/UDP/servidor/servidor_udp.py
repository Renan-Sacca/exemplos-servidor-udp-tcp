import socket
import json
import pika
from udp import decodificador

#Conexão rabbit
conexao = pika.BlockingConnection (pika.ConnectionParameters ( host ='localhost' ))
channel = conexao.channel ()

#Conexão servidor
HOST = "localhost"
PORT = 5000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST,PORT)
udp.bind(orig)

while True:
    #Mensagem do cliente
    msg, client = udp.recvfrom(1024)
    msg = msg.decode()

    #decodificar a mensagem e criar arquivo json
    dados = decodificador.decodificar(msg)
    a = json.dumps(dados[0])

    #Publicar json
    channel.basic_publish(exchange='renan', routing_key='testerenan', body=a)

    #Resposta do servidor
    ack = ">RER00:" + str(dados[1]) + ";" + str(dados[1]) + "<"
    udp.sendto(ack.encode(), client)

udp.close()






