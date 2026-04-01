#!/bin/bash

# Robson explica: Este script cria a pasta ssl e gera um certificado auto-assinado

echo "🔒 Iniciando a geração dos certificados SSL..."

# Cria a pasta caso ela não exista
mkdir -p ./nginx/ssl

# Gera a chave e o certificado válidos por 365 dias
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ./nginx/ssl/key.pem \
  -out ./nginx/ssl/cert.pem \
  -subj "/C=BR/ST=SP/L=Atibaia/O=UniFAAT/OU=ADS/CN=localhost"

echo "✅ Certificados gerados com sucesso na pasta ./nginx/ssl/"