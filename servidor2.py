import socket, threading

def handle_client(client_conn):
    while True:
        data = client_conn.recv(1024)
        if(not data):
            print(client_conn.getpeername(), 'disconectou-se')
            return
        client_conn.send(b'Eco=>' + data) # enviar msg para o mesmo cliente que mandou
        print(data)
        d = input("").encode()
        client_conn.send(b'Eco=> servidor ' + d)
with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reutilizar porta logo após servidor terminal, evita a excepcao 'OSError: [Errno 98] Address already in use'
    s.bind(('', 5000))
    s.listen(5)
    while True: 
        conexao, endereco = s.accept() # a espera de conexao
        print('Server conectado por', endereco)
        threading.Thread(target=handle_client, args=(conexao,)).start() # comecar thread para lidar com o cliente, uma para cada cliente

