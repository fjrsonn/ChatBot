from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Conversa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)
    resposta = db.Column(db.Text, nullable=False)
    data = db.Column(db.String(50), nullable=False)

