from flask import Flask, jsonify
import yaml
import os

# Importações dos módulos
from healthchecks.http_check import check_http
from healthchecks.db_check import check_database
from healthchecks.tcp_check import check_tcp
from models.alerts import AlertManager
from models.metrics import MetricsManager

app = Flask(__name__)
alert_manager = AlertManager()
metrics_manager = MetricsManager()

previous_status = {}

def load_config():
    config_path = os.environ.get('CONFIG_PATH', '../config/healthchecks.yml')
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        return {"healthchecks": {}}

@app.route('/health/status')
def health_status():
    return jsonify({"status": "healthy", "service": "api-backend"}), 200

@app.route('/metrics')
def metrics():
    config = load_config()
    healthchecks = config.get('healthchecks', {})
    
    results = {}
    overall_status = "healthy"
    
    for service_name, service_config in healthchecks.items():
        check_type = service_config.get('type')
        
        # 1. Executa o teste correto
        if check_type == 'http':
            result = check_http(service_config)
        elif check_type == 'database':
            result = check_database(service_config)
        elif check_type == 'tcp':
            result = check_tcp(service_config)
        else:
            result = {"status": "unknown", "response_time_ms": 0, "error": "Tipo não suportado"}
            
        current_status = result['status']
        response_time = result.get('response_time_ms', 0)
        
        # 2. Atualiza o status geral
        if current_status == "unhealthy":
            overall_status = "unhealthy"

        # 3. Lógica de Alertas
        last_status = previous_status.get(service_name, "healthy")
        if current_status == "unhealthy" and last_status != "unhealthy":
            alert_manager.trigger_alert(service_name, result.get('error', 'Falha desconhecida'))
        previous_status[service_name] = current_status

        # 4. Registra no Histórico
        metrics_manager.record_metric(service_name, current_status, response_time)
        
        # 5. Mescla os resultados do momento com os dados históricos
        stats = metrics_manager.get_service_stats(service_name)
        results[service_name] = {
            "current_status": current_status,
            "response_time_ms": response_time,
            "uptime": stats["uptime_percentage"],
            "history": stats["history"]
        }

    return jsonify({
        "overall_status": overall_status,
        "services": results
    }), 200

if __name__ == '__main__':
    # Em um ambiente local, liberamos CORS de forma rústica se necessário, 
    # mas o Docker vai gerenciar as portas.
    app.run(host='0.0.0.0', port=5000)