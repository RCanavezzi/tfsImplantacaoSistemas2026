#!/bin/bash

echo "=== Iniciando o Deploy da Barbearia BeGods ==="

# 1. Instalação do Nginx
echo "1. Instalando Nginx..."
sudo apt update -y
sudo apt install nginx -y

# 2. Criando o diretório web e copiando os arquivos
echo "2. Copiando arquivos do site para /var/www/begods..."
sudo mkdir -p /var/www/begods
sudo cp -r ~/TF01/website/* /var/www/begods/

# 3. Aplicando as boas práticas do Professor (Permissões)
echo "3. Ajustando permissões de segurança..."
# Transfere a propriedade da pasta para o seu usuário atual (evita uso de sudo para editar)
sudo chown -R $USER:$USER /var/www/begods

# Permissão 755 para diretórios (Dono faz tudo, Grupo e Outros só leem/executam)
find /var/www/begods -type d -exec chmod 755 {} \;

# Permissão 644 para arquivos (Dono lê/escreve, Grupo e Outros só leem)
find /var/www/begods -type f -exec chmod 644 {} \;

# 4. Configurando o Virtual Host no Nginx
echo "4. Aplicando configuração do Virtual Host..."
# Copia nosso arquivo site.conf para a pasta do Nginx
sudo cp ~/TF01/nginx/site.conf /etc/nginx/sites-available/begods.conf

# Cria o link simbólico para ativar o site
sudo ln -sf /etc/nginx/sites-available/begods.conf /etc/nginx/sites-enabled/

# Remove a configuração padrão do Nginx para evitar conflitos na porta 80
sudo rm -f /etc/nginx/sites-enabled/default

# 5. Reiniciando os serviços
echo "5. Reiniciando o Nginx..."
sudo systemctl enable nginx
sudo systemctl restart nginx

echo "=== Deploy concluído com sucesso! ==="
echo "Acesse http://localhost no seu navegador."
