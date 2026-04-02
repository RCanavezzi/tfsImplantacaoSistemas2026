#!/bin/bash
set -e

echo "=== INICIANDO LIMPEZA DE RECURSOS ==="

# Remover containers parados
echo "Removendo containers parados..."
docker container prune -f

# Remover redes não utilizadas
echo "Removendo redes sem uso..."
docker network prune -f

# Limpeza completa (CUIDADO!)
echo "Atenção: Removendo todas as imagens e volumes não utilizados..."
# O comando docker system prune af-volumes remove TUDO que não está sendo usado[cite: 314].
docker system prune -a -f --volumes 

echo "=== LIMPEZA CONCLUÍDA ==="
# Verificar espaço liberado [cite: 329]
docker system df