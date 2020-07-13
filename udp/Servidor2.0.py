import socket
import json
import pika
from udp import decodificador


conexao = pika.BlockingConnection (pika.ConnectionParameters ( host ='localhost' ))
channel = conexao.channel ()
HOST = "localhost"
PORT = 5000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST,PORT)
udp.bind(orig)

while True:
    msg, client = udp.recvfrom(1024)
    msg = msg.decode()
    dados = decodificador.decodificar(msg)
    a = json.dumps(dados[0])
    print(a)
    channel.basic_publish(exchange='renan', routing_key='testerenan', body=a)

    ack = ">RER00:" + str(dados[1]) + ";" + str(dados[1]) + "<"
    udp.sendto(ack.encode(), client)

udp.close()






