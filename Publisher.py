import pika,json


class UserEncoder(json.JSONEncoder):

    def default(self, obj):
        return obj.__dict__


class Correo:
    def __init__(self,para,asunto,cuerpo):
        self.para=para
        self.asunto=asunto
        self.cuerpo=cuerpo



##Se crea un array de objetos
"""pendiente para implementar"""
correos=[]
correos.append(Correo("rafael","probando","hola rafael esto es un mensaje de prueba"))
correos.append(Correo("juan","probando2","esto es otra pruba de django"))
"""----------------------------------------------------------------------"""


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
co={'para' : 'rafael_eltezo@hotmail.com', 'de': 'barboza.rafael.p@gmail.com', 'cuerpo':'esto es un mensaje'}


##se serializa el objeto con python
serialize = json.dumps(correos, cls=UserEncoder, indent=4)


# Connect and block other rabbit
channel = connection.channel()
# agregando el canal de comunicacion
channel.queue_declare(queue="importers")
# Make importers
channel.basic_publish(
    exchange="",
    routing_key="importers",
    body=json.dumps(co)
)

print("Finalizado")

connection.close()