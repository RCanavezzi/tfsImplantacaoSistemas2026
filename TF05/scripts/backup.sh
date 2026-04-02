#!/bin/bash
set -e

BACKUP_DIR=$1
if [ -z "$BACKUP_DIR" ]; then
    BACKUP_DIR="backups/$(date +%Y%m%d_%H%M%S)"
fi

echo "=== INICIANDO BACKUP EM $BACKUP_DIR ==="
mkdir -p "$BACKUP_DIR"

# Backup do Banco de Dados (exemplo via dump)
echo "Fazendo dump do banco de dados..."
docker exec database-app mysqldump -u user -ppass app > "$BACKUP_DIR/db_backup.sql" || echo "Aviso: DB não está rodando."

# Backup das configurações
echo "Copiando arquivos de configuração..."
cp -r config/ "$BACKUP_DIR/"

echo "=== BACKUP FINALIZADO COM SUCESSO ==="