import json

import pika

connection=pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel=connection.channel()
channel.exchange_declare(
    exchange='logs',
    exchange_type='direct'
    )
result=channel.queue_declare(exclusive=True)
queue_name=result.method.queue
channel.queue_bind(exchange='logs',queue=queue_name,routing_key='error')
channel.queue_bind(exchange='logs',queue=queue_name,routing_key='info')
channel.queue_bind(exchange='logs',queue=queue_name,routing_key='warning')
channel.queue_bind(exchange='logs',queue=queue_name,routing_key='debug')


print ("[*] staring worken with queue{}".format(queue_name))


def callback(ch,method,properties,body):

    #print ("[*] Messager for broker{}:{}".format(queue_name,body))
    cuerpo = json.loads(body)
    print("creando archivo")
    f = open('logs.txt', 'a')
    f.write("["+cuerpo['tipo']+"] "+"'"+cuerpo['codigo']+"' "+"<"+cuerpo['cuerpo']+">")
    f.close()


channel.basic_consume(callback,queue=queue_name,no_ack=True)
print("inicio de worker")
channel.start_consuming()
