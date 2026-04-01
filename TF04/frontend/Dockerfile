# Usa uma imagem oficial e leve do Node.js
FROM node:alpine

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copia os arquivos da sua pasta admin (como o index.html) para dentro do container
COPY . .

# Instala o 'serve', um pacote simples para servir arquivos estáticos
RUN npm install -g serve

# Avisa o Docker que este container vai usar a porta 3000
EXPOSE 3000

# Comando que inicia o servidor na porta 3000
CMD ["serve", "-s", ".", "-l", "3000"]