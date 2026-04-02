import os
import yaml
import requests
import smtplib
from email.message import EmailMessage

class AlertManager:
    def __init__(self):
        # Quando a classe for iniciada, ela carrega as configurações
        self.alerts_config = self._load_yaml('alerts.yml')
        self.thresholds_config = self._load_yaml('thresholds.yml')

    def _load_yaml(self, filename):
        """Função auxiliar para ler os arquivos YAML da pasta config."""
        config_path = os.environ.get('CONFIG_DIR', '../config/')
        full_path = os.path.join(config_path, filename)
        
        try:
            with open(full_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Aviso: Arquivo de configuração {filename} não encontrado.")
            return {}

    def send_webhook(self, message):
        """Dispara uma mensagem HTTP POST para a URL configurada."""
        # Busca a configuração de webhook com fallback para dicionários vazios
        webhook_config = self.alerts_config.get('alerts', {}).get('webhook', {})
        
        if not webhook_config.get('enabled'):
            return

        url = webhook_config.get('url')
        if url:
            try:
                # O formato json={"text": message} é o padrão aceito pelo Slack
                requests.post(url, json={"text": message}, timeout=5)
                print(f"✅ Webhook enviado com sucesso: {message}")
            except Exception as e:
                print(f"❌ Erro ao enviar webhook: {e}")

    def send_email(self, subject, message):
        """Dispara um e-mail utilizando SMTP."""
        email_config = self.alerts_config.get('alerts', {}).get('email', {})
        
        if not email_config.get('enabled'):
            return

        try:
            # Monta a estrutura do e-mail
            msg = EmailMessage()
            msg.set_content(message)
            msg['Subject'] = subject
            msg['From'] = email_config.get('username')
            # Transforma a lista de destinatários em uma string separada por vírgula
            msg['To'] = ", ".join(email_config.get('recipients', []))

            # Conecta ao servidor (exemplo: smtp.gmail.com)
            server = smtplib.SMTP(email_config.get('smtp_server'), email_config.get('smtp_port'))
            server.starttls() # Inicia conexão segura
            server.login(email_config.get('username'), email_config.get('password'))
            server.send_message(msg)
            server.quit()
            
            print(f"📧 E-mail de alerta enviado para os administradores.")
        except Exception as e:
            print(f"❌ Erro ao enviar e-mail: {e}")

    def trigger_alert(self, service_name, issue_description):
        """
        Função principal que a API vai chamar quando um serviço cair.
        Ela dispara tanto o webhook quanto o e-mail, se estiverem habilitados.
        """
        alert_msg = f"🚨 ALERTA CRÍTICO: O serviço '{service_name}' reportou um problema.\nDetalhes: {issue_description}"
        
        # Dispara as notificações em paralelo (no fluxo síncrono aqui por simplicidade)
        self.send_webhook(alert_msg)
        self.send_email(f"Alerta de Sistema: Falha em {service_name}", alert_msg)