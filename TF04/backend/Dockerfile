# Usa a imagem oficial do Node.js (versão leve)
FROM node:18-alpine

# Define a pasta de trabalho dentro do container
WORKDIR /usr/src/app

# Copia os arquivos de dependência primeiro (otimiza o cache do Docker)
COPY package*.json ./

# Instala as dependências
RUN npm install

# Copia o resto do código (o app.js)
COPY . .

# Expõe a porta que configuramos no app.js
EXPOSE 5000

# Comando para iniciar a API
CMD ["npm", "start"]