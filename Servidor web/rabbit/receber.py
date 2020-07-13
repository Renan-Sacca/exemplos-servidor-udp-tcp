import pika
#criar conexao
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
#criar fila caso n exista, evitar de dar erro
#channel.queue_declare(queue='testerenan')

#função para receber o conteudo da fila
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

#definindo qual a fila que a função ira chamar
channel.basic_consume(
    queue='testerenan', on_message_callback=callback, auto_ack=True)

print('[*] Aguardando mensagens. Para sair, pressione CTRL + C')
#inicia um loop recebendo todas mensagens
channel.start_consuming()