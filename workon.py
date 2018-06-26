import pika,json
from envio import message as men

connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue="importers")

def importers(ch, method, properties, body):
    ##ch.basic_ack()
    ##cuerpo=json.load(body)
    print(body)
    cuerpo=json.loads(body)
    men('woken', cuerpo['para'], cuerpo['de'], cuerpo['cuerpo'])




channel.basic_consume(importers, queue="importers", no_ack=True) ##si se requiere que envie una respuesta se pone no_ack=False

print("inicio del worker")

channel.start_consuming()

