import tornado.web
import tornado.websocket
import tornado.ioloop
import time
import threading
import pika

def callback(ch, method, properties, body):
    global mensagem_rabbit
    mensagem_rabbit = (" [x] Recebi mensagem %r" % body)
    for i in range(0, len(conexoes)):
        mensagem_rabbit += ", de cliente numero " + str(i)
        conexoes[i].write_message(mensagem_rabbit)
        time.sleep(1)

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    global conexoes
    def open(self):
        print("Novo cliente conectado")
        conexoes.append(self)

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("Cliente desconectado")

    def check_origin(self, origin):
        return True

def handle_client(channel):
    global d , conexoes
    channel.start_consuming()

mensagem_rabbit = ""
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.basic_consume(queue='testerenan', on_message_callback=callback, auto_ack=True)

threading.Thread(target=handle_client, args=(channel,)).start()

application = tornado.web.Application([(r"/", WebSocketHandler),])
conexoes = []

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()