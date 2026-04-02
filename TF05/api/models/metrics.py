from datetime import datetime

class MetricsManager:
    def __init__(self, max_history=60):
        # Dicionário para armazenar o histórico de cada serviço
        # max_history define quantos pontos no tempo vamos guardar (ex: últimos 60 testes)
        self.history = {}
        self.max_history = max_history

    def record_metric(self, service_name, status, response_time):
        """Salva o resultado de um teste no histórico do serviço."""
        if service_name not in self.history:
            self.history[service_name] = []
        
        self.history[service_name].append({
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "status": status,
            "response_time_ms": response_time
        })
        
        # Remove o item mais antigo se ultrapassar o limite (janela deslizante)
        if len(self.history[service_name]) > self.max_history:
            self.history[service_name].pop(0)

    def get_service_stats(self, service_name):
        """Calcula o uptime e retorna o histórico para os gráficos."""
        records = self.history.get(service_name, [])
        if not records:
            return {"uptime_percentage": "100.0%", "history": []}
        
        # Conta quantos registros estão saudáveis
        successful = sum(1 for r in records if r["status"] == "healthy")
        
        # Regra de três básica para achar a porcentagem
        uptime = (successful / len(records)) * 100
        
        return {
            "uptime_percentage": f"{uptime:.1f}%",
            "history": records
        }