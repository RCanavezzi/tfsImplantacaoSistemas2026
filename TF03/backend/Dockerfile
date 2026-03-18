# Usa uma imagem oficial do Node.js leve (alpine)
FROM node:18-alpine

# Define a pasta de trabalho dentro do container
WORKDIR /usr/src/app

# Copia os ficheiros de dependências primeiro (ajuda no cache do Docker)
COPY package*.json ./

# Instala as dependências (express, mysql2, cors)
RUN npm install

# Copia o resto do código (o nosso app.js)
COPY . .

# Expõe a porta 5000, conforme exigido na tarefa
EXPOSE 5000

# O comando para iniciar a nossa API
CMD ["node", "app.js"]