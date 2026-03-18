# Arquitetura do Sistema - TF03

Este documento descreve a arquitetura multi-container orquestrada via Docker Compose para o sistema de Blog.

## Visão Geral

O sistema segue uma arquitetura baseada em microsserviços, dividida em quatro componentes principais que comunicam entre si através de uma rede Docker isolada.

### 1. Proxy Reverso (`nginx-proxy`)
- **Tecnologia:** Nginx (Alpine)
- **Porta Host:** `80`
- **Responsabilidade:** Atua como o único ponto de entrada do sistema (Load Balancer/Proxy Reverso). Ele recebe todas as requisições na porta 80 e as direciona:
  - Requisições para `/` são enviadas para o serviço **frontend**.
  - Requisições para `/api/` e `/health` são enviadas para o serviço **backend**.
- **Volumes:** Mapeia o ficheiro `nginx.conf` como somente leitura e possui um volume para persistência de logs (`nginx-logs`).

### 2. Frontend (`frontend`)
- **Tecnologia:** HTML, CSS, JavaScript puro (servidos por Nginx)
- **Porta Interna:** `3000`
- **Responsabilidade:** Fornecer a interface gráfica ao utilizador. Faz requisições assíncronas (via `fetch`) para o proxy, que as redireciona para a API.

### 3. Backend API (`backend`)
- **Tecnologia:** Node.js com Express e MySQL2
- **Porta Interna:** `5000`
- **Responsabilidade:** Processar a lógica de negócio e fornecer endpoints RESTful (CRUD). Conecta-se diretamente ao banco de dados utilizando variáveis de ambiente injetadas pelo Docker Compose.

### 4. Banco de Dados (`database`)
- **Tecnologia:** MySQL 8.0
- **Porta Interna:** `3306` (Não exposta ao Host, apenas à rede interna)
- **Responsabilidade:** Armazenamento e persistência dos dados (postagens).
- **Volumes:** Utiliza o volume nomeado `blog-data` para garantir que os dados não sejam perdidos caso o container seja reiniciado ou destruído. Utiliza um script `init.sql` para criar a tabela inicial no primeiro arranque.

## Rede e Isolamento (`blog-network`)

Todos os containers operam numa rede Docker do tipo `bridge` chamada `blog-network`. O Docker fornece um servidor DNS interno que permite aos containers comunicarem-se utilizando os nomes dos serviços (ex: o backend conecta-se ao banco de dados através do hostname `database`). 

Apenas a porta 80 do Nginx Proxy está exposta para a máquina hospedeira, garantindo segurança e encapsulamento dos serviços internos.