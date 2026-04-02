import requests
import time

def check_http(config):
    # Pega o tempo inicial para calcular a métrica de performance (Response Time)
    start_time = time.time()
    url = config.get('url')
    expected_status = config.get('expected_status', 200)
    timeout = int(config.get('timeout', '5s').replace('s', '')) # Converte '10s' para 10

    try:
        # Faz a requisição HTTP
        response = requests.get(url, timeout=timeout)
        
        # Calcula o tempo gasto em milissegundos
        response_time = round((time.time() - start_time) * 1000, 2)
        
        # Verifica se o status retornado é o que esperávamos (ex: 200 OK)
        if response.status_code == expected_status:
            return {"status": "healthy", "response_time_ms": response_time, "error": None}
        else:
            return {"status": "unhealthy", "response_time_ms": response_time, "error": f"Status {response.status_code}"}
            
    except Exception as e:
        return {"status": "unhealthy", "response_time_ms": 0, "error": str(e)}