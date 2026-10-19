import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações de e-mail obtidas dos Secrets do GitHub
EMAIL_USER = os.environ.get("GMAIL_USER")
EMAIL_PASS = os.environ.get("GMAIL_PASSWORD")

# Relatório executivo de preços atualizado com links diretos
assunto = "📊 Relatório Diário: Melhores Preços Pampers Pants XG com Links"
corpo_email = """
Olá! Aqui está o resumo diário de preços, custos por tira e links diretos das fraldas Pampers Pants XG:

🏆 MELHORES OFERTAS E LINKS:

1. 🟢 Pampers Pants Premium Care XG (64 un. - Drogaria São Paulo)
   • Preço Efetivo: R$ 1,20 / tira (via mecânica Leve 2 + Retirada em loja)
   • Link: https://www.drogariasaopaulo.com.br/fraldas-pampers-pants-premium-care-top-xg-64-unidades/p

2. 🔵 Pampers Pants Ajuste Total XG (132 un. - Amazon Brasil)
   • Preço Efetivo: R$ 1,24 / tira (com cupom + frete Prime)
   • Link: https://amzn.achados.me/nDZLhb7

3. 🔵 Pampers Pants Ajuste Total XG (82 un. - Drogasil)
   • Preço Efetivo: R$ 1,34 / tira (via mecânica Leve Mais Pague Menos + Retirada)
   • Link: https://www.drogasil.com.br/campanha-trd-pampers-51946.html

📦 PONTOS DE ATENÇÃO:
• Lembre-se de informar o seu CEP e selecionar a retirada em loja nas farmácias para zerar o frete.
• Verifique se os cupons de desconto continuam ativos na página de checkout.

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
        print("E-mail diário com links enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    enviar_email()
