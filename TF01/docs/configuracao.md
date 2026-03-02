# Documentação de Configuração e Segurança

## 1. Configuração do Nginx
- Nginx instalado via gerenciador de pacotes (`apt`).
- Virtual Host configurado e linkado na pasta `sites-enabled`.
- O site padrão (`default`) foi desativado para evitar conflitos na porta 80.
- Serviço configurado para iniciar automaticamente no boot (`systemctl enable nginx`).

## 2. Configuração de Logs e Erros
- **Logs de acesso:** `/var/log/nginx/begods_access.log`
- **Logs de erro:** `/var/log/nginx/begods_error.log`
- Página 404 customizada configurada no Virtual Host para capturar rotas inexistentes.

## 3. Boas Práticas de Segurança e Permissões
Para evitar o uso perigoso e desnecessário do comando `sudo` durante o desenvolvimento diário, aplicamos a transferência de propriedade e o princípio do menor privilégio:
- **Propriedade (`chown`):** O diretório `/var/www/begods` pertence ao usuário atual do sistema, permitindo a edição segura dos arquivos web.
- **Permissão de Pastas (`chmod 755`):** O dono tem controle total; o servidor Nginx (e outros) apenas leem e acessam as pastas.
- **Permissão de Arquivos (`chmod 644`):** O dono edita os arquivos; o servidor Nginx apenas tem permissão de leitura para exibi-los no navegador.
