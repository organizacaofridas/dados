FROM python:3.11-slim

# Define diretório de trabalho dentro do container
WORKDIR /app

# Copia e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Porta padrão do Cloud Run
ENV PORT=8080

# Comando de entrada
CMD exec gunicorn --bind :$PORT --workers 2 app:app
