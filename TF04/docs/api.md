# Documentação da API REST - Sistema de Blog

Esta API foi desenvolvida em Node.js com Express e permite o gerenciamento completo (CRUD) das postagens do blog. Todas as respostas são no formato JSON.

## Endpoints Disponíveis

### 1. Health Check
Verifica se a API está online e a funcionar.
- **URL:** `/health`
- **Método:** `GET`
- **Resposta de Sucesso (200 OK):** `OK`

### 2. Listar Todos os Posts
Retorna uma lista com todas as postagens, ordenadas da mais recente para a mais antiga.
- **URL:** `/api/posts`
- **Método:** `GET`
- **Resposta de Sucesso (200 OK):**
  ```json
  [
    {
      "id": 1,
      "title": "Meu Primeiro Post",
      "content": "Olá mundo!...",
      "created_at": "2026-03-17T12:00:00.000Z"
    }
  ]
  ```

### 3. Obter Post Específico
Retorna os detalhes de uma postagem específica baseada no seu ID.
- **URL:** `/api/posts/:id`
- **Método:** `GET`
- **Resposta de Sucesso (200 OK):** Objeto JSON do post.
- **Resposta de Erro (404 Not Found):** `{"error": "Post não encontrado"}`

### 4. Criar Novo Post
Cria uma nova postagem no banco de dados.
- **URL:** `/api/posts`
- **Método:** `POST`
- **Corpo da Requisição (JSON):**
  ```json
  {
    "title": "Título da Postagem",
    "content": "Conteúdo da postagem..."
  }
  ```
- **Resposta de Sucesso (201 Created):** Retorna o ID do post criado.

### 5. Atualizar Post
Atualiza o título e o conteúdo de uma postagem existente.
- **URL:** `/api/posts/:id`
- **Método:** `PUT`
- **Corpo da Requisição (JSON):**
  ```json
  {
    "title": "Título Atualizado",
    "content": "Conteúdo atualizado..."
  }
  ```
- **Resposta de Sucesso (200 OK):** `{"message": "Post atualizado com sucesso!"}`

### 6. Deletar Post
Remove permanentemente uma postagem do banco de dados.
- **URL:** `/api/posts/:id`
- **Método:** `DELETE`
- **Resposta de Sucesso (200 OK):** `{"message": "Post deletado com sucesso!"}`