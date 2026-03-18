const express = require('express');
const mysql = require('mysql2/promise'); // Usamos promise para facilitar o código assíncrono
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json()); // Permite ler dados no formato JSON enviados pelo Frontend

// Configuração da ligação ao banco de dados usando as variáveis do docker-compose.yml
const dbConfig = {
    host: process.env.DB_HOST || 'database',
    user: process.env.DB_USER || 'bloguser',
    password: process.env.DB_PASSWORD || 'blogpass',
    database: process.env.DB_NAME || 'blogdb'
};

// --- ENDPOINTS (ROTAS) OBRIGATÓRIOS ---

// 1. GET /health - Health check (Verifica se a API está viva)
app.get('/health', (req, res) => {
    res.status(200).send('OK');
});

// 2. GET /api/posts - Listar todos os posts
app.get('/api/posts', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [rows] = await connection.execute('SELECT * FROM posts ORDER BY created_at DESC');
        await connection.end();
        res.json(rows);
    } catch (error) {
        res.status(500).json({ error: 'Erro ao buscar posts: ' + error.message });
    }
});

// 3. GET /api/posts/:id - Obter post específico
app.get('/api/posts/:id', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [rows] = await connection.execute('SELECT * FROM posts WHERE id = ?', [req.params.id]);
        await connection.end();
        
        if (rows.length === 0) return res.status(404).json({ error: 'Post não encontrado' });
        res.json(rows[0]);
    } catch (error) {
        res.status(500).json({ error: 'Erro ao buscar o post.' });
    }
});

// 4. POST /api/posts - Criar novo post
app.post('/api/posts', async (req, res) => {
    const { title, content } = req.body;
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [result] = await connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)', [title, content]);
        await connection.end();
        res.status(201).json({ id: result.insertId, title, content });
    } catch (error) {
        res.status(500).json({ error: 'Erro ao criar post.' });
    }
});

// 5. PUT /api/posts/:id - Atualizar post
app.put('/api/posts/:id', async (req, res) => {
    const { title, content } = req.body;
    try {
        const connection = await mysql.createConnection(dbConfig);
        await connection.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', [title, content, req.params.id]);
        await connection.end();
        res.json({ message: 'Post atualizado com sucesso!' });
    } catch (error) {
        res.status(500).json({ error: 'Erro ao atualizar post.' });
    }
});

// 6. DELETE /api/posts/:id - Deletar post
app.delete('/api/posts/:id', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        await connection.execute('DELETE FROM posts WHERE id = ?', [req.params.id]);
        await connection.end();
        res.json({ message: 'Post deletado com sucesso!' });
    } catch (error) {
        res.status(500).json({ error: 'Erro ao deletar post.' });
    }
});

// Inicialização do servidor na porta 5000 (exposta internamente)
const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Backend a rodar na porta ${PORT}`);
});