import asyncio
import random
import websockets
import pika, threading


def callback(ch, method, properties, body):
    global d
    d = (" [x] Recebi %r" % body)



def handle_client(channel):
    global d
    while True:
        d = channel.start_consuming()

async def time(websocket, path):
    global d
    while True:
        await websocket.send(d)
        await asyncio.sleep(4)
d = ""
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.basic_consume(
    queue='testerenan', on_message_callback=callback, auto_ack=True)

threading.Thread(target=handle_client, args=(channel,)).start()

start_server = websockets.serve(time, "127.0.0.1", 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()