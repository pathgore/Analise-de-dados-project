from flask import Flask, render_template
from flask_socketio import SocketIO, send

aplicativo = Flask(__name__)
SocketIO = SocketIO(aplicativo, cors_allowed_origins="*")
@SocketIO.on("message")
def gerenciar_mensagem(mensagem):
   send(mensagem, broadcast=True)
@aplicativo.route("/")
def homepage():
   return render_template("index.html")

SocketIO.run(aplicativo, host="localhost", debug="true")
