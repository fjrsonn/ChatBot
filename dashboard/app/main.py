from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dashboard.app.routes import bp 


db = SQLAlchemy()

class Conversa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)
    resposta = db.Column(db.Text, nullable=False)
    data = db.Column(db.String(50), nullable=False)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatbot.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(bp)

with app.app_context():
    db.create_all()
    if not Conversa.query.first():
        exemplo = [
            Conversa(usuario='usuario_01', mensagem='Oi!', resposta='Olá! Como posso ajudar?', data='2025-04-18 15:00'),
            Conversa(usuario='usuario_02', mensagem='Qual horário de atendimento?', resposta='Das 08h às 18h.', data='2025-04-18 15:10'),
        ]
        db.session.bulk_save_objects(exemplo)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')







