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
    return send_file(sinal, mimetype = sinal.content_type)