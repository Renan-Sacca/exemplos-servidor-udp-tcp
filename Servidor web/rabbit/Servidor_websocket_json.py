import tornado.web
import tornado.websocket
import tornado.ioloop
import threading
import pika
import json

def verificar_novo(dado):
    for i in range(0,len(configuracao)):
        if dado == configuracao[i]:
            print()


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

    def on_close(self):
        print("Cliente desconectado")
        excluir_conexao(self)

    def on_message(self, message):
        dados_json = json.loads(message)
        n = verificar_novo(dados_json)
        if n == 0:
            self.write_message(u"You said: " + message)
        else:
            configuracao.append(dados_json)


    def check_origin(self, origin):
        return True

"""Função que a thread ficara rodando para consumir as mensagem em segundo plano"""
def procurar_mensagens(channel):
    channel.start_consuming()

"""Variaveis"""
mensagem_rabbit = ""
conexoes = []
configuracao = []

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