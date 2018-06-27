import json
from envio import message as men
import pika

connection=pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel=connection.channel()
channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
    )
result=channel.queue_declare(exclusive=True)
queue_name=result.method.queue
channel.queue_bind(exchange='logs',queue=queue_name)

print ("[*] staring worken with queue{}".format(queue_name))

def callback(ch,method,properties,body):
    print ("[*] Messager for broker{}:{}".format(queue_name,body))
    cuerpo = json.loads(body)
    if cuerpo['tipo']=='error':
        men('\n' +'woken', cuerpo['para'], cuerpo['de'], 'Ha ocurrido un error '+cuerpo['cuerpo']+'\n')
        print("mensaje enviado")

channel.basic_consume(callback,queue=queue_name,no_ack=True)
print("inicio de worker")
channel.start_consuming()
