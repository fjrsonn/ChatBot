
# 🤖 Chatbot Multicanal com Flask, Telegram e WhatsApp

Este projeto é um chatbot modular e extensível com suporte a múltiplos canais: API Flask, terminal, Telegram e WhatsApp.

## 📦 Funcionalidades
- Classificação de intenções com Machine Learning (Naive Bayes).
- API REST com Flask.
- Conectores para Telegram (`python-telegram-bot`) e WhatsApp (Twilio).
- Interface interativa via terminal.
- Arquitetura modular e testável.
- Script único para inicializar tudo com um clique.

## 🚀 Como usar

### 1. Instale as dependências
```bash
pip install -r requirements.txt
```

### 2. Configure variáveis de ambiente
Crie um arquivo `.env` com:
```env
TELEGRAM_TOKEN=seu_token_do_bot
```

### 3. Treine o modelo
```bash
python -m core.trainer
```

### 4. Inicie 
```bash
python run_all.py
```

## 🧪 Testes
Execute os testes com:
```bash
pytest tests/
```

## 📁 Estrutura do Projeto
```
chatbot/
├── app/
│   ├── __init__.py
│   ├── main.py              # Inicialização da API Flask
│   └── routes.py            # Endpoints da API
├── bots/
│   ├── telegram_bot.py
│   ├── whatsapp_bot.py
│   └── chatbot_interface.py # Interface de terminal
├── core/
│   ├── __init__.py
│   ├── chat.py              # Processamento de mensagem
│   ├── model.py             # Carregamento do modelo
│   ├── trainer.py           # Treinamento com sklearn
│   └── utils.py             # Utilitários (limpeza de texto etc.)
├── data/
│   └── intents.json         # Dados de treino
├── model/
│   └── classifier.pkl       # Modelo treinado
├── tests/
│   ├── test_chat.py
│   └── test_model.py
├── run_all.py               # Script único de inicialização
├── requirements.txt
├── Instrucoes.txt
├── Projeto.txt
├── .env
└── README.md
```

## 📌 Requisitos
- Python 3.8+
- Conta no [Telegram BotFather](https://t.me/BotFather)
- Conta Twilio (opcional para WhatsApp)

---
