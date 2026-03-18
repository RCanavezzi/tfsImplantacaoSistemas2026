FROM nginx:alpine
# Copiar para a pasta padrão do Nginx
COPY . /usr/share/nginx/html
# Mudar a porta padrão do Nginx do container para 3000
RUN sed -i 's/80/3000/g' /etc/nginx/conf.d/default.conf
EXPOSE 3000