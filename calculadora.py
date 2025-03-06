from flask import Flask, jsonify, request
from flask_cors import CORS
import math as mt

app = Flask(__name__)
CORS(app)

def error_response(mensaje):
    return jsonify({"Error": mensaje}), 400

@app.route("/suma")
@app.route("/<numero1>/<numero2>")
def suma(numero1=0, numero2=0):
    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
        resultado = numero1 + numero2
        return jsonify({"Resultado": resultado, "Operacion": "suma"})
    except ValueError:
        return error_response("Parámetros no válidos para la operación")

@app.route("/resta/<numero1>/<numero2>")
def resta(numero1=0, numero2=0):
    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
        resultado = numero1 - numero2
        return jsonify({"Resultado": resultado, "Operacion": "resta"})
    except ValueError:
        return error_response("Parámetros no válidos para la operación")

@app.route("/multiplicacion/<numero1>/<numero2>")
def multiplicacion(numero1=0, numero2=0):
    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
        resultado = numero1 * numero2
        return jsonify({"Resultado": resultado, "Operacion": "multiplicación"})
    except ValueError:
        return error_response("Parámetros no válidos para la operación")

@app.route("/division/<numero1>/<numero2>")
def division(numero1=0, numero2=0):
    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
        if numero2 == 0:
            return error_response("División por cero no permitida")
        resultado = numero1 / numero2
        return jsonify({"Resultado": resultado, "Operacion": "división"})
    except ValueError:
        return error_response("Parámetros no válidos para la operación")

@app.route("/potenciacion/<numero1>/<numero2>")
def potenciacion(numero1=0, numero2=0):
    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
        resultado = numero1 ** numero2
        return jsonify({"Resultado": resultado, "Operacion": "potenciación"})
    except ValueError:
        return error_response("Parámetros no válidos para la operación")

@app.route("/seno/<numero1>")
def seno(numero1=0):
    try:
        numero1 = float(numero1)
        resultado = mt.sin(numero1)  
        return jsonify({"Resultado": resultado, "Operacion": "seno"})
    except ValueError:
        return error_response("Parámetro no válido para la operación")

@app.route("/coseno/<numero1>")
def coseno(numero1=0):
    try:
        numero1 = float(numero1)
        resultado = mt.cos(numero1)  
        return jsonify({"Resultado": resultado, "Operacion": "coseno"})
    except ValueError:
        return error_response("Parámetro no válido para la operación")

if __name__ == '__main__':
    app.run(debug=True)
    