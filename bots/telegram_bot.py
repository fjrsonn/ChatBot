import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    CommandHandler,
    filters
)
from core.chat import get_response

# Função para lidar com mensagens recebidas
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = get_response(user_input)  # Gera a resposta com base na entrada do usuário
    await update.message.reply_text(response)  # Envia a resposta de volta ao usuário

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Sou o chatbot. Como posso te ajudar?")

# Função principal para iniciar o bot do Telegram
def start_telegram_bot():
    TOKEN = os.getenv("TELEGRAM_TOKEN")  # Token pode ser definido como variável de ambiente

    if not TOKEN:
        raise ValueError("⚠️  Token do Telegram não encontrado. Defina a variável TELEGRAM_TOKEN.")

    app = ApplicationBuilder().token(TOKEN).build()

    # Comandos e mensagens
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot do Telegram iniciado...")

    try:
        app.run_polling()  # Inicia o bot com polling
    except Exception as e:
        print(f"Erro ao iniciar o bot: {e}")


