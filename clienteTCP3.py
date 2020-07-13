import socket, select, sys

with socket.socket() as s: # por default ja abre socket AF_INET e TCP (SOCK_STREAM)
    s.connect(('', 5000))
    while True:
        io_list = [sys.stdin, s]
        ready_to_read,ready_to_write,in_error = select.select(io_list , [], [])   # visto que as funcoes input e recv sao 'bloqueadoras' da execucao do codigo seguinte temos de 'seguir' ambos os eventos desta maneira
        if s in ready_to_read: # caso haja dados a chegar
            data = s.recv(1024)
            if(not data): # ex: caso o servidor se desligue, ou conexao perdida
                break
            print(data.decode())  # decode/encode por default e utf-8
        else: # enviar msg
            msg = sys.stdin.readline() # capturar mensagem inserida no terminial, no command prompt
            s.send(msg.encode())  # decode/encode por default e utf-8
            sys.stdout.flush()
