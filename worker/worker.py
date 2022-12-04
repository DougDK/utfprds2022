import pika, sys, os
from testeCGNE import teste_cgne
from testeCGNR import teste_cgnr

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='images')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        tipo=body.decode("utf-8").split('/')[0]
        usuario=body.decode("utf-8").split('/')[1]
        file_name=body.decode("utf-8").split('/')[2]
        newpath = "C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/imagensprocessadas/{}".format(usuario)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        if(tipo=="CGNE"):
            print("Processando CGNE")
            teste_cgne(file_name, usuario)
        elif(tipo=="CGNR"):
            print("Processando CGNR")
            teste_cgnr(file_name, usuario)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        return        

    channel.basic_consume(queue='images', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)