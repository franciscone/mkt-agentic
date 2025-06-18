# Dockerfile
FROM python:3.11-slim

# Evita erros com dependências
RUN apt-get update && apt-get install -y build-essential curl

# Cria pasta de trabalho
WORKDIR /app

# Copia dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o código
COPY . .

# Comando padrão
CMD ["python", "src/main.py"]
