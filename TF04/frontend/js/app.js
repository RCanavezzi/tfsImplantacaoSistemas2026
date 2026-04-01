// URL base da nossa API (graças ao proxy reverso do Nginx, usamos apenas /api/posts)
const API_URL = '/api/posts';

// Função para listar os posts na página inicial
async function carregarPosts() {
    try {
        const resposta = await fetch(API_URL);
        const posts = await resposta.json();
        const container = document.getElementById('lista-posts');
        
        if (posts.length === 0) {
            container.innerHTML = '<p>Nenhum post encontrado. Cria o primeiro!</p>';
            return;
        }

        container.innerHTML = posts.map(post => `
            <div class="post-card">
                <h2>${post.title}</h2>
                <p>${post.content.substring(0, 100)}...</p>
                <a href="post.html?id=${post.id}" class="btn">Ler Mais</a>
            </div>
        `).join('');
    } catch (erro) {
        console.error('Erro ao carregar posts:', erro);
    }
}

// Função para criar um novo post
async function criarPost(event) {
    event.preventDefault(); // Evita que a página recarregue
    const title = document.getElementById('titulo').value;
    const content = document.getElementById('conteudo').value;

    try {
        await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, content })
        });
        window.location.href = 'index.html'; // Volta para a página inicial
    } catch (erro) {
        alert('Erro ao criar post!');
    }
}