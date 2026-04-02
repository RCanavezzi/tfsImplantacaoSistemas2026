import socket
import time

def check_tcp(config):
    start_time = time.time()
    
    # Extrai o host e a porta do arquivo de configuração
    host = config.get('host')
    port = int(config.get('port', 6379)) # Default para Redis se não for informado
    
    # Limpa a string de timeout (ex: '5s' vira 5)
    timeout_str = str(config.get('timeout', '5s')).replace('s', '')
    timeout = int(timeout_str)

    try:
        # Cria um socket de rede IPv4 (AF_INET) e TCP (SOCK_STREAM)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        
        # Tenta conectar. Se conseguir, a porta está aberta e o serviço está respondendo!
        sock.connect((host, port))
        sock.close()
        
        response_time = round((time.time() - start_time) * 1000, 2)
        return {"status": "healthy", "response_time_ms": response_time, "error": None}
        
    except Exception as e:
        # Se a conexão for recusada ou der timeout, o serviço está doente
        return {"status": "unhealthy", "response_time_ms": 0, "error": str(e)}