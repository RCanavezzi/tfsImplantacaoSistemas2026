# TF04 - E-commerce com Load Balancer Avançado


## Aluno

- **Nome:** Ronaldo Canavezzi

- **RA:** 6324536

- **Curso:** Análise e Desenvolvimento de Sistemas


## Arquitetura
- **Nginx:** Load balancer com SSL e rate limiting configurados (`least_conn`).
- **Backend:** 3 instâncias da API Node.js para alta disponibilidade, com rota `/api/info` retornando o Hostname.
- **Frontend:** Loja virtual estática servida na porta 3000 internamente.
- **Admin:** Painel administrativo rodando isolado e roteado via proxy reverso.

## Funcionalidades Implementadas
- ✅ Load balancing com algoritmo least_conn
- ✅ Health checks automáticos (via `max_fails` e fail_timeout no Nginx)
- ✅ Failover transparente
- ✅ SSL/TLS com certificado auto-assinado (gerado via script)
- ✅ Rate limiting para proteção (`limit_req_zone`)
- ✅ Logs detalhados com upstream info (`$upstream_addr`)
- ✅ Compressão gzip
- ✅ Virtual hosts

## Como Executar

### Pré-requisitos
- Docker e Docker Compose
- Terminal Bash (para execução do script SSL)

### Execução
```bash
# 1. Dar permissão e gerar certificados SSL
chmod +x ./scripts/generate-ssl.sh
./scripts/generate-ssl.sh

# 2. Subir todos os serviços (Nginx, 3x Backend, Frontend, Admin)
docker-compose up -d --build

# 3. Verificar status
docker-compose ps

# Teste de load balancing (Com a flag -k para ignorar o aviso do certificado local)
for i in {1..10}; do curl -k -s https://localhost/api/info; done

# Clone o repositório

git clone https://github.com/RCanavezzi/tfsImplantacaoSistemas2026.git

cd TF034

# Subir todos os serviços

docker-compose up -d --build


# Verificar status

docker-compose ps


# Acessar aplicação

# Frontend: http://localhost

# API: http://localhost/api/posts


Funcionalidades
✅ Listar posts existentes

✅ Visualizar post individual

✅ Criar novo post

✅ Editar post existente

✅ Deletar post

Endpoints da API
GET /api/posts - Lista todos os posts

POST /api/posts - Cria novo post

GET /api/posts/:id - Obtém post específico

PUT /api/posts/:id - Atualiza post

DELETE /api/posts/:id - Remove post

Comandos Úteis
# Ver logs de todos os serviços

docker-compose logs -f


# Ver logs de serviço específico

docker-compose logs -f backend


# Parar todos os serviços

docker-compose down


# Parar e remover volumes

docker-compose down -v


Persistência
Dados do banco: Volume blog-data

Logs do Nginx: Volume nginx-logs

Dados sobrevivem a restart dos containers


## Entrega


### Repositório GitHub

- **Nome:** `tfsImplantacaoSistemas2026`

- **Pasta:** `TF04/`

- **Visibilidade:** Público


### Validação

```bash

# Teste completo

docker-compose up -d --build

curl http://localhost/api/posts

docker-compose down