from flask import Flask, request, send_file
from testeCGNE import teste_cgne

app = Flask(__name__)

@app.route("/", methods=['GET'])
def live():
    return ""

@app.route("/reconstrucaosinal", methods=['POST'])
def reconstrucaoSinal():
    sinal = request.files['sinal']
    sinal.save('./sinais/{}'.format(sinal.filename))
    teste_cgne(sinal.filename)
    return ""


@app.route("/sinal", methods=['GET'])
def sinal():
    processed = open('./imagensprocessadas/{}.jpeg'.format(request.json['nome']),'rb')
    return send_file(processed, mimetype = "image/jpeg")