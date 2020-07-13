import socket

HOST = "localhost"
PORT = 5000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print("conectando")
msg = input("Digite : ").encode()
while msg != ("\x18".encode()):
	udp.sendto(msg,dest)
	a = (udp.recv(1024).decode())
	print(a)
	msg = input("Digite : ").encode()
	#data = udp.recv(1024)

udp.close()


"""
>REV071960475265-2221562-0496541200000112;BL=3800;SV=5;ID=10754;IO=335;AD=6903.1<
"""