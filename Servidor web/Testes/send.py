
import pika

#criando conexao
conexão = pika.BlockingConnection (pika.ConnectionParameters ( host ='localhost' ))
channel = conexão.channel ()

#criando fila
#channel.queue_declare (queue = 'testerenan')

#exchange é o nome da troca
#routing key nome da fila
a = input("Conteudo do corpo: ")
while a != "":
    channel.basic_publish (exchange = 'renan',
                          routing_key = 'testerenan',
                          body = a)
    print ( "[x] Enviado ",a )
    a = input("Conteudo do corpo: ")
conexão.close ()