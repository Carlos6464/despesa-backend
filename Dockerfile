# Usa uma imagem oficial leve do Python
FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Impede o Python de criar arquivos .pyc e força o log imediato (bom para Docker)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala dependências do sistema necessárias para o psycopg2 (Postgres)
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do projeto para dentro do container
COPY . .

# Expõe a porta 8000
EXPOSE 8000

# Comando para rodar a API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]