# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo de dependências para o container
COPY app/requirements.txt /app/requirements.txt

# Instalar as dependências
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar o conteúdo da aplicação para o container
COPY app /app

# Expôr a porta 8000
EXPOSE 8000

# Comando para iniciar o servidor FastAPI com Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
