# TF03 - Sistema de Blog Multi-Container


## Aluno

- **Nome:** Ronaldo Canavezzi

- **RA:** 6324536

- **Curso:** Análise e Desenvolvimento de Sistemas


## Arquitetura

- **Nginx Proxy:** Load balancer e proxy reverso

- **Frontend:** Interface web (HTML/CSS/JS)

- **Backend:** API REST (Python/Node.js/PHP)

- **Database:** MySQL com persistência


## Como Executar


### Pré-requisitos

- Docker e Docker Compose instalados


### Execução

```bash

# Clone o repositório

git clone [URL_DO_SEU_REPO]

cd TF03


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

- **Pasta:** `TF03/`

- **Visibilidade:** Público


### Validação

```bash

# Teste completo

docker-compose up -d --build

curl http://localhost/api/posts

docker-compose down