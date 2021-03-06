#Aula 06 - Métodos HTTP

from flask import Flask, request
from json import dumps

app = Flask(__name__, static_folder='static')


@app.route('/add', methods=["POST", "GET"])
def add():
    if request.method == "POST":
        return dumps(request.form)
    return "OKOK GET "


#método simples para entender POST e GET vindos do navegador
'''@app.route('/add', methods=["POST", "GET"])
def add():
    if request.method == "POST":
        return "OKOK POST"
    return "OKOK GET OU OUTRO"
'''




if __name__ == '__main__':
    app.run(debug=True)