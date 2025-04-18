from dashboard.app.models import Conversa  # Corrigindo o caminho de importação
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/admin')
def admin_dashboard():
    conversas = Conversa.query.order_by(Conversa.id.desc()).all()
    return render_template('dashboard.html', conversas=conversas)

print("Arquivo routes.py foi carregado corretamente")




