from flask import Flask, request, send_file
import pika
import os

app = Flask(__name__)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='images')

@app.route("/", methods=['GET'])
def live():
    return ""

@app.route("/reconstrucaosinal", methods=['POST'])
def reconstrucaoSinal():
    sinal = request.files['sinal']
    sinal.save('./sinais/{}'.format(sinal.filename))
    if(request.form['tipo']=="CGNE"):
        channel.basic_publish(exchange='', routing_key='images', body='CGNE/{}/{}'.format(request.form["usuario"], sinal.filename))
    elif(request.form['tipo']=="CGNR"):
        channel.basic_publish(exchange='', routing_key='images', body='CGNR/{}/{}'.format(request.form["usuario"], sinal.filename))
    return ""


@app.route("/sinal", methods=['GET'])
def sinal():
    processed = open('./imagensprocessadas/{}/{}'.format(request.json['usuario'], request.json['nome']),'rb')
    return send_file(processed, mimetype = "image/jpeg")

@app.route("/listarsinais", methods=['GET'])
def listarsinais():

    abs_path = os.path.join("imagensprocessadas", request.json["usuario"])

    sinais = os.listdir(abs_path)
    print(sinais)
    return {"sinais":sinais}