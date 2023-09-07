import math
from flask import Flask, request, redirect, url_for, render_template, make_response, jsonify
from Utilitários.Sensores import isSensoresPressionados, lerSensores
from Algoritmos.KNN import KNN
from Algoritmos.Modelos.Modelos import ImportarModelo
import time


app = Flask(__name__)
timerInicial = 0
modeloIA = ImportarModelo("KNNModel.algumaextensãoqueeuesquecinomomentoedepoisautalizoporaqui")


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('postura.html')


@app.route("/recPostura/", methods=['GET', 'POST'])
def recPostura():
    global timerInicial
    lstSensoresLeituras = lerSensores()
    if isSensoresPressionados(lstSensoresLeituras):
        if timerInicial == 0:
            timerInicial = time.time()
        global modeloIA
        posturaAtual = KNN.reconhecer(lstSensoresLeituras, modeloIA)
        timerAtual = time.time() - timerInicial
        resposta = {
            'Timer': math.floor(timerAtual),
            'Postura': posturaAtual
        }
    else:
        timerInicial = 0
        resposta = {
            'Timer': 0,
            'Postura': 'Não há ninguém sentado na cadeira no momento'}
    return jsonify(resposta)


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
