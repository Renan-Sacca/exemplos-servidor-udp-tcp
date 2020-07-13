import socket
HOST= "localhost"
PORT = 5000
tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
origem = (HOST,PORT)
tcp.bind(origem)
tcp.listen(2)
print("[*] Escutando {}:{}".format(HOST,PORT))
while True:
	con, cliente = tcp.accept()
	
	print("CLiente :",cliente)
	while True:
		msg=con.recv(1024)
		if not msg: break
		print(cliente, msg)
	print("finalizando conexao do cliente",cliente)
	con.close()
