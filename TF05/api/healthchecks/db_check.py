import pymysql
import time
from urllib.parse import urlparse

def check_database(config):
    start_time = time.time()
    # Pega a string de conexão: "mysql://user:pass@db:3306/app"
    connection_string = config.get('connection')
    query = config.get('query', 'SELECT 1')
    
    try:
        # Fazendo o parse da URL de conexão para pegar usuário, senha, host, etc.
        parsed = urlparse(connection_string)
        
        # Conectando ao banco de dados
        connection = pymysql.connect(
            host=parsed.hostname,
            user=parsed.username,
            password=parsed.password,
            database=parsed.path.lstrip('/'),
            port=parsed.port or 3306,
            connect_timeout=5
        )
        
        # Executando a query de teste
        with connection.cursor() as cursor:
            cursor.execute(query)
            cursor.fetchone()
        
        connection.close()
        response_time = round((time.time() - start_time) * 1000, 2)
        return {"status": "healthy", "response_time_ms": response_time, "error": None}
        
    except Exception as e:
        return {"status": "unhealthy", "response_time_ms": 0, "error": str(e)}