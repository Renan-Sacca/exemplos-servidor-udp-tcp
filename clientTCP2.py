import socket
HOST = "localhost"
PORT=5000
tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
dest = (HOST,PORT)
tcp.connect(dest)
print("---\n")
msg = input("Escreva: ").encode()
while msg != ('x'.encode()):
	data = tcp.recv(1024)  
	print(data)
	tcp.send (msg)
	msg=input("escreva: ").encode()
tcp.close()


