
import pika

#criando conexao
conexão = pika.BlockingConnection (pika.ConnectionParameters ( host ='localhost' ))
channel = conexão.channel ()
#criando fila
#channel.queue_declare (queue = 'testerenan')
#exchange é o nome da troca
#routing key nome da fila
i=0
while i <1000:
    channel.basic_publish (exchange = 'renan',
                          routing_key = 'testerenan',
                          body = str(i))
    print("[x] Enviado ", i)
    i+=1

print ( "[x] Enviado ",i )
conexão.close ()