# TF05 - Sistema de Monitoramento e Automação

## Aluno
- **Nome:** [RONALDO CANAVEZZI]
- **RA:** [6324536]
- **Curso:** Análise e Desenvolvimento de Sistemas - UniFAAT

## Funcionalidades Implementadas
- Healthchecks inteligentes avançados (HTTP, TCP, Database) com resposta de performance.
- Dashboard visual de monitoramento em tempo real (HTML/CSS/JS).
- API em Python (Flask) para coleta e histórico de métricas.
- Sistema de alertas e gatilhos (email, webhook) baseado em mudanças de estado.
- Automação completa de containers utilizando Docker Compose.
- Scripts de manutenção avançados (Backup automatizado, Limpeza Segura, Rollback e Monitoramento via Terminal).

## Como Executar

### Pré-requisitos
- Docker e Docker Compose instalados.
- Ambiente Bash (Linux/Mac/WSL/Git Bash) para os scripts de automação.

### Passos para Execução

1. **Subir a infraestrutura e API:**
   ```bash
   docker compose up -d --build