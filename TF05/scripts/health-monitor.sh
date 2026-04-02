#!/bin/bash

# Define a URL da nossa API de métricas
API_URL="http://localhost:5000"

# Função para exibir o relatório de saúde completo
show_report() {
    echo "=== RELATÓRIO DE SAÚDE DOS SERVIÇOS ==="
    echo "Data/Hora: $(date '+%Y-%m-%d %H:%M:%S')"
    echo "---------------------------------------"
    
    # Verifica se o jq está instalado
    if ! command -v jq &> /dev/null; then
        echo "⚠️ Aviso: O formatador 'jq' não foi encontrado. Exibindo JSON bruto."
        HAS_JQ=false
    else
        HAS_JQ=true
    fi

    # Tenta conectar na API silenciosamente
    if curl -s "$API_URL/health/status" > /dev/null; then
        echo "🌐 API de Monitoramento: ONLINE"
        echo "Métricas detalhadas:"
        
        if [ "$HAS_JQ" = true ]; then
            curl -s "$API_URL/metrics" | jq '{Status_Geral: .overall_status, Servicos: .services}'
        else
            curl -s "$API_URL/metrics"
            echo "" # Adiciona quebra de linha no final
        fi
    else
        echo "❌ API de Monitoramento: OFFLINE (Containers não iniciados ou porta 5000 fechada)"
        echo "Exibindo status nativo do Docker:"
        # Atualizado para o formato novo do Docker Compose (com espaço) conforme seu Lab
        docker compose ps
    fi
    echo "======================================="
}

# Processamento dos argumentos passados via terminal
case "$1" in
    --report)
        show_report
        ;;
        
    --watch)
        echo "Iniciando monitoramento em tempo real (Pressione Ctrl+C para sair)..."
        watch -n 2 "$0 --report"
        ;;
        
    --test-alerts)
        echo "Simulando teste de alertas..."
        echo "Por favor, para testar alertas reais, pare um container executando:"
        echo "docker compose stop db"
        echo "A API detectará a falha na próxima checagem!"
        ;;
        
    --pre-deploy|--check-all)
        echo "Verificando saúde de todos os serviços para deploy..."
        
        if curl -s "$API_URL/health/status" > /dev/null; then
            # Se não tiver JQ, fazos um grep simples no JSON
            if [ "$HAS_JQ" = true ]; then
                STATUS=$(curl -s "$API_URL/metrics" | jq -r '.overall_status')
            else
                STATUS=$(curl -s "$API_URL/metrics" | grep -o '"overall_status":"[^"]*"' | cut -d'"' -f4)
            fi
            
            if [ "$STATUS" = "healthy" ]; then
                echo "✅ Todos os serviços estão saudáveis. Seguro para prosseguir."
                exit 0
            else
                echo "❌ CUIDADO: O status geral é '$STATUS'. Deploy abortado."
                exit 1
            fi
        else
             echo "❌ API Offline. Impossível validar serviços pré-deploy."
             exit 1
        fi
        ;;
        
    --check)
        SERVICE=$2
        if [ -z "$SERVICE" ]; then
            echo "Erro: Forneça o nome do serviço. Ex: ./scripts/health-monitor.sh --check backend"
            exit 1
        fi
        echo "Verificando serviço específico: $SERVICE..."
        if docker compose ps | grep "$SERVICE" | grep -q "(healthy)"; then
            echo "✅ Serviço $SERVICE está saudável."
            exit 0
        else
            echo "❌ Serviço $SERVICE NÃO está saudável ou não foi encontrado."
            exit 1
        fi
        ;;
        
    *)
        echo "Uso: $0 {--report|--watch|--test-alerts|--pre-deploy|--check <serviço>|--check-all}"
        exit 1
        ;;
esac