import tornado.web
import tornado.websocket
import tornado.ioloop
import threading
import pika
import json

def verificar_novo(se):
    for i in range(0,len(configuracao)):
        if "" == configuracao[i] and se == conexoes[i]:
            del(configuracao[i])
            return 1
    return 0

def excluir_conexao(endereco):
    for i in range(0,len(conexoes)):
        if conexoes[i] == endereco:
            del(conexoes[i])
            del(configuracao[i])
            break

""" Função para procurar mensagens no rabbit e retornar para os clientes"""
def callback(ch, method, properties, body):
    menssagem_rabbit = json.loads(body)
    for i in range(0, len(conexoes)):
        if (configuracao[i]["ras_eve_id_indice"]) == (menssagem_rabbit["ras_eve_id_indice"]):
            conexoes[i].write_message(menssagem_rabbit)
            break



""" Classe de conexao com cliente"""
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("Novo cliente conectado")
        conexoes.append(self)
        configuracao.append("")

    def on_close(self):
        print("Cliente desconectado")
        excluir_conexao(self)

    def on_message(self, message):

        n = verificar_novo(self)
        if n == 0:
            self.write_message(u"You said: " + message)
        else:
            dados_json = json.loads(message)
            configuracao.append(dados_json)
            self.write_message(u"Usuario conectado " + dados_json["id_usuario"])


    def check_origin(self, origin):
        return True

"""Função que a thread ficara rodando para consumir as mensagem em segundo plano"""
def procurar_mensagens():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.basic_consume(queue='testerenan', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

"""Variaveis"""
conexoes = []
configuracao = []

"""Chamando a Thread"""
threading.Thread(target=procurar_mensagens, args=()).start()

"""Conexão do WebSocket"""
application = tornado.web.Application([(r"/", WebSocketHandler),])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()