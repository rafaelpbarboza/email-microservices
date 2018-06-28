from celery import Celery
from envio import message

app=Celery("example1",backend="amqp://guest@localhost",broken="amqp://localhost")

@app.task()
def correo(subject, to, from_email, msj):
        message(subject, to, from_email, msj)
        return True