const express = require('express');
const cors = require('cors');
const os = require('os'); // Biblioteca nativa para pegar informações da máquina

const app = express();
app.use(cors());
app.use(express.json());

// --- ENDPOINTS PARA O TF04 ---

// 1. GET /health - Endpoint de Health Check (Exigido pelo professor)
// O Nginx vai usar esta rota para saber se a instância está viva e saudável
app.get('/health', (req, res) => {
    res.status(200).send('OK');
});

// 2. GET /api/info - Prova de Load Balancing
// Esta é a rota mais importante para a sua nota! Ela devolve qual dos 3 containers respondeu.
app.get('/api/info', (req, res) => {
    res.json({
        mensagem: "Conectado com sucesso à API do E-commerce!",
        // os.hostname() vai retornar o ID único gerado pelo Docker para este container
        instance_id: os.hostname() 
    });
});

// 3. GET /api/produtos - Uma rota de produtos simulada (Mock)
// Apenas para o seu e-commerce não ficar vazio caso você queira puxar dados no frontend
app.get('/api/produtos', (req, res) => {
    res.json([
        { id: 1, nome: "Notebook Gamer", preco: 5500.00 },
        { id: 2, nome: "Smartphone Pro", preco: 3200.00 },
        { id: 3, nome: "Teclado Mecânico", preco: 450.00 }
    ]);
});

// Inicialização do servidor na porta 5000 (esperada pelo Nginx)
const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Backend rodando na porta ${PORT} | ID da Instância: ${os.hostname()}`);
});