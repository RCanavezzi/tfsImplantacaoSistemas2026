// URL da nossa API local mapeada no docker-compose
const API_URL = 'http://localhost:5000/metrics';

async function fetchMetrics() {
    try {
        const response = await fetch(API_URL);
        const data = await response.json();
        updateDashboard(data);
    } catch (error) {
        console.error("Erro ao buscar métricas:", error);
        document.getElementById('overall-status').className = 'status-card unhealthy';
        document.querySelector('#overall-status .status-text').innerText = 'API Offline';
    }
}

function updateDashboard(data) {
    // 1. Atualiza o Status Geral
    const overallCard = document.getElementById('overall-status');
    overallCard.className = `status-card ${data.overall_status}`;
    document.querySelector('#overall-status .status-text').innerText = 
        data.overall_status === 'healthy' ? 'Sistema Saudável' : 'Falha Detectada';

    // 2. Atualiza os cards individuais baseado nos nomes definidos no YAML
    const services = data.services;

    if(services['web-frontend']) {
        document.getElementById('frontend-uptime').innerText = services['web-frontend'].uptime;
        document.getElementById('frontend-response').innerText = services['web-frontend'].response_time_ms + 'ms';
        updateIndicator('frontend-status', services['web-frontend'].current_status);
    }

    if(services['api-backend']) {
        document.getElementById('backend-uptime').innerText = services['api-backend'].uptime;
        document.getElementById('backend-response').innerText = services['api-backend'].response_time_ms + 'ms';
        updateIndicator('backend-status', services['api-backend'].current_status);
    }

    if(services['database']) {
        document.getElementById('database-uptime').innerText = services['database'].uptime;
        // Para banco de dados, se estiver healthy, simulamos conexões ok, caso contrário 0
        document.getElementById('database-connections').innerText = 
            services['database'].current_status === 'healthy' ? 'Conectado' : 'Falha';
        updateIndicator('database-status', services['database'].current_status);
    }
}

function updateIndicator(elementId, status) {
    // Procura a "bolinha" de status dentro do card e muda a cor
    const indicator = document.querySelector(`#${elementId} .status-indicator`);
    if(indicator) {
        indicator.className = `status-indicator ${status}`;
    }
}

// Inicia a primeira busca e depois agenda para repetir a cada 5 segundos
fetchMetrics();
setInterval(fetchMetrics, 5000);