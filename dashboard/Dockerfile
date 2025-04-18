FROM python:3.10-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo requirements.txt e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o diretório do código para o container
COPY ./dashboard /app

# Comando para rodar a aplicação Flask
CMD ["python", "-m", "dashboard.app.main"]




