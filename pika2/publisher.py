import json
import sys
import pika

connection=pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel=connection.channel()
channel.exchange_declare(exchange='logs',exchange_type='fanout')

co={'tipo':'info','codigo':'25255255','para' : 'rafael_eltezo@hotmail.com', 'de': 'barboza.rafael.p@gmail.com', 'cuerpo':'esto es un mensaje'}
#messege=''.join(sys.argv[1:]) or 'info:hello word'
print("enviando log")

channel.basic_publish(
    exchange="logs",
    routing_key="",
    body=json.dumps(co)
)
#print("[*] sent message: {}".format(messege))

connection.close()