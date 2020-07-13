import tornado.web
import tornado.websocket
import tornado.ioloop
import threading
import pika
import json

def verificar_novo(se):
    for i in range(0,len(conexao_lista)):
        if se == conexao_lista[i]["endereco"]:
            return 0
    return 1

def excluir_conexao(endereco):
    for i in range(0,len(conexao_lista)):
        if conexao_lista[i]["endereco"] == endereco:
            del(conexao_lista[i])
            break

""" Função para procurar mensagens no rabbit e retornar para os clientes"""
def callback(ch, method, properties, body):
    menssagem_rabbit = json.loads(body)
    threading.Lock()
    for i in range(0, len(conexao_lista)):
        if (conexao_lista[i]["configuracao"]["ras_eve_id_indice"]) == (menssagem_rabbit["ras_eve_id_indice"]):
            conexao_lista[i]["endereco"].write_message(menssagem_rabbit)
            break
    threading.RLock()



""" Classe de conexao com cliente"""
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("Novo cliente conectado")


    def on_close(self):
        print("Cliente desconectado")
        excluir_conexao(self)

    def on_message(self, message):

        n = verificar_novo(self)
        if n == 0:
            self.write_message(u"Sua menssagem: " + message)
        else:
            dados_json = json.loads(message)
            conexao_dicionario["endereco"] = self
            conexao_dicionario["configuracao"] = dados_json
            conexao_lista.append(conexao_dicionario.copy())
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
conexao_lista = []
conexao_dicionario = {"endereco": "","configuracao":""}


"""Chamando a Thread"""
threading.Thread(target=procurar_mensagens, args=()).start()

"""Conexão do WebSocket"""
application = tornado.web.Application([(r"/", WebSocketHandler),])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()