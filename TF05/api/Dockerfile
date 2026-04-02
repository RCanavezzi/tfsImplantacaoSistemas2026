FROM python:3.9-slim

WORKDIR /app

# O SEGREDO: Instalando o curl no Linux do container para o healthcheck funcionar!
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]