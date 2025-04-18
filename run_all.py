import multiprocessing
from bots.chatbot_interface import run_chatbot
from bots.telegram_bot import start_telegram_bot
from bots.whatsapp_bot import whatsapp_app
from threading import Thread
from waitress import serve
from dotenv import load_dotenv

load_dotenv()

def run_flask():
    from app import create_app
    app = create_app()
    try:
        serve(app, port=5000)
    except Exception as e:
        print(f"Erro ao iniciar o Flask: {e}")

def run_whatsapp():
    try:
        serve(whatsapp_app, port=5001)
    except Exception as e:
        print(f"Erro ao iniciar o WhatsApp: {e}")

def run_telegram():
    try:
        start_telegram_bot()
    except Exception as e:
        print(f"Erro ao iniciar o bot do Telegram: {e}")

def run_chatbot_terminal():
    try:
        run_chatbot()
    except Exception as e:
        print(f"Erro no chatbot de terminal: {e}")

if __name__ == "__main__":
    try:
        # Inicia os processos
        multiprocessing.Process(target=run_flask).start()
        multiprocessing.Process(target=run_whatsapp).start()
        multiprocessing.Process(target=run_telegram).start()
        Thread(target=run_chatbot_terminal).start()
    except Exception as e:
        print(f"Erro ao iniciar o sistema: {e}")
