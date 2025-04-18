from core.chat import get_response

def run_chatbot():
    print("Chatbot iniciado! (digite 'sair' para encerrar)")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            break
        print("Bot:", get_response(user_input))
