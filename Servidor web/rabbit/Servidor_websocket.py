import tornado.web
import tornado.websocket
import tornado.ioloop
import time
import threading
import pika

""" Função para procurar mensagens no rabbit e retornar para os clientes"""
def callback(ch, method, properties, body):
    mensagem_rabbit = (" [x] Recebi mensagem %r" % body)
    for i in range(0, len(conexoes)):
        mensagem_imprimir = mensagem_rabbit + ", de cliente numero " + str(i)
        conexoes[i].write_message(mensagem_imprimir)


""" Classe de conexao com cliente"""
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("Novo cliente conectado")
        conexoes.append(self)

    def on_close(self):
        print("Cliente desconectado")

    def check_origin(self, origin):
        return True

"""Função que a thread ficara rodando para consumir as mensagem em segundo plano"""
def procurar_mensagens(channel):
    channel.start_consuming()

"""Variaveis"""
mensagem_rabbit = ""
conexoes = []

"""Definição de configuração para a conexão com rabbit"""
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.basic_consume(queue='testerenan', on_message_callback=callback, auto_ack=True)

"""Chamando a Thread"""
threading.Thread(target=procurar_mensagens, args=(channel,)).start()

"""Conexão do WebSocket"""
application = tornado.web.Application([(r"/", WebSocketHandler),])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()