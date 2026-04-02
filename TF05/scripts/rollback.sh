#!/bin/bash
set -e

BACKUP_DIR=$1

if [ -z "$BACKUP_DIR" ] || [ ! -d "$BACKUP_DIR" ]; then
    echo "Erro: Diretório de backup não fornecido ou inválido."
    exit 1
fi

echo "=== INICIANDO ROLLBACK A PARTIR DE $BACKUP_DIR ==="

# Restaurando o banco de dados
echo "Restaurando banco de dados..."
cat "$BACKUP_DIR/db_backup.sql" | docker exec -i database-app mysql -u user -ppass app

# Parar serviços novos e subir a versão antiga (simulação de rollback de imagem)
echo "Revertendo containers..."
docker-compose down
docker-compose up -d --build

echo "=== ROLLBACK FINALIZADO ==="