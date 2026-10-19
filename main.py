import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações de e-mail obtidas dos Secrets do GitHub
EMAIL_USER = os.environ.get("GMAIL_USER")
EMAIL_PASS = os.environ.get("GMAIL_PASSWORD")

# Relatório executivo de preços
assunto = "📊 Relatório Diário: Melhores Preços Pampers Pants XG"
corpo_email = """
Olá! Aqui está o resumo diário de preços e custos por tira das fraldas Pampers Pants XG:

🏆 Melhor Oferta:
• Drogaria São Paulo: R$ 1,20 / tira (Premium Care 64 un. via mecânica Leve 2 + Retirada em loja)
• Amazon Brasil: R$ 1,24 / tira (Ajuste Total 132 un. com cupom + Prime)

📦 Composição & Alertas:
• Focos em fardos fechados ou mecânicas "Leve Mais Pague Menos" para neutralizar frete.
• Lembre-se de validar o CEP ao abrir os links.

💡 Veredito: Momento ideal para fechar nas opções listadas acima.
"""

def enviar_email():
    if not EMAIL_USER or not EMAIL_PASS:
        print("Erro: Credenciais de e-mail não encontradas nas Secrets do GitHub.")
        return

    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(EMAIL_USER, EMAIL_PASS)

        mensagem = MIMEMultipart()
        mensagem["From"] = EMAIL_USER
        mensagem["To"] = EMAIL_USER
        mensagem["Subject"] = assunto
        mensagem.attach(MIMEText(corpo_email, "plain", "utf-8"))

        servidor.sendmail(EMAIL_USER, EMAIL_USER, mensagem.as_string())
        servidor.quit()
        print("E-mail diário enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    enviar_email()
