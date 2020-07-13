import tornado.web
import tornado.websocket
import tornado.ioloop


import json



class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("Novo cliente conectado")
        conexoes.append(self)

    def on_close(self):
        print("Cliente desconectado")

    def on_message(self, message):
        self.write_message(u"You said: " + message)
        print(message)
        dados_json = json.loads(message)
        print(dados_json["ras_eve_id_indice"])

        self.write_message(dados_json)
        configuracao.append(dados_json)

    def check_origin(self, origin):
        return True


conexoes = []
configuracao = []

"""Conexão do WebSocket"""
application = tornado.web.Application([(r"/", WebSocketHandler),])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()