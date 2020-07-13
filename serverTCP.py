import socket
import threading

bind_ip = 'localhost'
bind_port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)
print ('[*] Escutando {}:{}'.format(bind_ip,bind_port))
def handle_client(client_socket):
	request = client_socket.recv(1024)
	print ('[*] Recebido: {}'.format(request))
	print ('\n--------------\n')
	client_socket.send(('\n Mensagem destinada ao cliente: %s\n' %addr[0]).encode())	 
	client_socket.send(('\n ACK! \n Recebido pelo servidor!\n').encode())
	client_socket.close()
while True:
	client, addr = server.accept()
	print ('[*] Conexao aceita de: {}:{}'.format(addr[0], addr[1]))
	client_handler = threading.Thread(target=handle_client, args=(client,))
	client_handler.start()
