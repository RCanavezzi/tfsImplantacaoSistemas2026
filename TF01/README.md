# TF01 - BeGods Barbearia

## Aluno
- **Nome:** [RONALDO CANAVEZZI]
- **RA:** [6324536]
- **Curso:** Análise e Desenvolvimento de Sistemas

## Empresa Fictícia
- **Nome:** BeGods Barbearia
- **Ramo:** Barbearia Profissional e Estética Masculina
- **Descrição:** Muito mais que uma barbearia, somos um espaço dedicado ao estilo e autoestima masculina, unindo técnicas tradicionais com as tendências mais modernas.

## Como Executar

### Pré-requisitos
- Ubuntu 20.04+ ou similar (WSL)
- Acesso sudo

### Instalação
```bash
# Clone o repositório
git clone https://github.com/RCanavezzi/tfsImplantacaoSistemas2026.git
cd tfsImplantacaoSistemas2026/TF01

# Dê permissão de execução e rode o script de instalação
chmod +x scripts/install.sh
cd scripts
./install.sh

## Acesso
- **Site principal:** http://localhost

- **Páginas disponíveis:**

- / (Home)

- /sobre.html

- /servicos.html

- /contato.html

# Configurações Aplicadas
- Nginx configurado com virtual host personalizado para a barbearia.

- Logs personalizados gerados em /var/log/nginx/ (begods_access.log e begods_error.log).

- Permissões configuradas de forma segura (Dono = Usuário atual, 644 para arquivos, 755 para diretórios).

- Página 404 customizada implementada.

# Verificar status do Nginx
sudo systemctl status nginx

# Ver logs de acesso
sudo tail -f /var/log/nginx/begods_access.log

# Ver logs de erro
sudo tail -f /var/log/nginx/begods_error.log
