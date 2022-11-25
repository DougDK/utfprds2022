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
        file_name=body.decode("utf-8").split('/')[1]
        if(tipo=="CGNE"):
            print("Processando CGNE")
            teste_cgne(file_name)
        elif(tipo=="CGNR"):
            print("Processando CGNR")
            teste_cgnr(file_name)
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