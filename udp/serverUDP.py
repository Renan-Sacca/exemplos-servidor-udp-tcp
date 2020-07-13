import socket
import json
import pika
conexao = pika.BlockingConnection (pika.ConnectionParameters ( host ='localhost' ))
channel = conexao.channel ()
def decodificar(msg):
	msg= msg[1:len(msg)-1]
	msg = msg.split(";")
	dados = {'header' : msg[0]}

	for i in range (1,len(msg)):
		dados_quebrados = msg[i].split("=")
		dados.update({dados_quebrados[0]: dados_quebrados[1]})

	return dados

HOST = "localhost"
PORT = 5000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST,PORT)
udp.bind(orig)

while True:
	msg, client = udp.recvfrom(1024)
	msg = msg.decode()
	dados = decodificar(msg)
	a = json.dumps(dados)
	print(a)
	channel.basic_publish(exchange='renan',
						  routing_key='testerenan',
						  body=a)
	ack = ">RER00:"+ dados["id"] + ";" + dados["id"] + "<"
	udp.sendto(ack.encode(), client)

#>REV071960475265-2221562-0496541200000112;latitude=55;longitude=66;id=5549236;data=15/05/2014;vel=100<

udp.close()
