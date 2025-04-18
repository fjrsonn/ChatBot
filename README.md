
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
Chatbot0.2/
├── .env
├── Instrucoes.txt
├── Modificacoes-futuras.txt
├── README.md
├── requirements.txt
├── run_all.py
├── app/
│   ├── main.py
│   ├── routes.py
│   └── __init__.py
├── bots/
│   ├── chatbot_interface.py
│   ├── telegram_bot.py
│   └── whatsapp_bot.py
├── core/
│   ├── chat.py
│   ├── model.py
│   └── trainer.py
```

## 📌 Requisitos
- Python 3.8+
- Conta no [Telegram BotFather](https://t.me/BotFather)
- Conta Twilio (opcional para WhatsApp)

📦 Bibliotecas externas:

    flask – framework web

    waitress – servidor WSGI para produção

    python-dotenv (dotenv) – para carregar variáveis do arquivo .env

    python-telegram-bot (telegram, telegram.ext) – integração com o Telegram

    twilio – integração com WhatsApp via Twilio

    scikit-learn – para o modelo de NLP (ex: Naive Bayes, vetorização de texto)

📦 Bibliotecas padrão do Python:

    os, threading, multiprocessing, random, json, re, pickle
---
