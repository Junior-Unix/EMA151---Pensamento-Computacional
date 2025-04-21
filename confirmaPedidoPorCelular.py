#  3. (RA1) Construa um programa em que sejam solicitados os seguintes dados:
#  Nome:
#  Celular:
#  Endereco:
#  Ao final da entrada dos dados, deve ser impressa a seguinte Mensagem:
#  Bom dia XXXXX, vocˆe em breve receber´ a uma mensagem pelo celular XXXXXXX confir
# mando o encaminhamento do seu pedido, sendo que o endere¸co de entrega que consta em
#  nosso cadastro ´e XXXXXXXX. Caso o mesmo n˜ ao corresponda solicitamos que entre em sua
#  conta pessoal e atualizar o seu cadastro.
#  Os dados devem ser impressos de acordo com o que foi digitado pela pessoa.

#  O nome deve ser impresso em letras mai´ usculas e o celular deve ser impresso
#  com o caractere “-” entre os dois primeiros d´ igitos e os dois ´ ultimos d´ igitos.
#  O endereco deve ser impresso com a primeira letra de cada palavra em mai´ uscula.
# while True:
#     nome = input("Digite o nome (ou '(q)uit' para encerrar): ")
#     if nome.lower() == 'q':
#         break
#     celular = input("Digite o celular com codigo de área, Exemplo '41999999999': ")
#     if not celular.isdigit() or len(celular) != 11:
#         print("Celular inválido. Deve conter 11 dígitos.")
#         continue
#     endereco = input("Digite o endereco: ")
#
#     nome_maiusculo = nome.upper()
#     celular_formatado = f"{celular[:2]}-{celular[2:7]}-{celular[7:]}"
#     endereco_formatado = ' '.join([palavra.capitalize() for palavra in endereco.split()])
#
#     print(f"\033[32;40mBom dia {nome_maiusculo}, você em breve receberá uma mensagem pelo celular {celular_formatado} confirmando o encaminhamento do seu pedido, sendo que o endereço de entrega que consta em nosso cadastro é {endereco_formatado}. Caso o mesmo não corresponda solicitamos que entre em sua conta pessoal e atualizar o seu cadastro.\033[m")
# Enviar uma mensagem de sms para o celular formatado
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, mensagem):
    remetente = 'nelson.leme@pucpr.edu.br'
    senha = 'senha_do_email'

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    msg.attach(MIMEText(mensagem, 'plain'))

    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())
        server.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Falha ao enviar e-mail: {e}")

while True:
    nome = input("Digite o nome (ou '(q)uit' para encerrar): ")
    if nome.lower() == 'q':
        break
    celular = input("Digite o celular com codigo de área, Exemplo '41999999999': ")
    if not celular.isdigit() or len(celular) != 11:
        print("Celular inválido. Deve conter 11 dígitos.")
        continue
    endereco = input("Digite o endereco: ")
    email = input("Digite o e-mail: ")

    nome_maiusculo = nome.upper()
    celular_formatado = f"{celular[:2]}-{celular[2:7]}-{celular[7:]}"
    endereco_formatado = ' '.join([palavra.capitalize() for palavra in endereco.split()])

    mensagem = (f"Bom dia {nome_maiusculo}, você em breve receberá uma mensagem pelo celular {celular_formatado} "
                f"confirmando o encaminhamento do seu pedido, sendo que o endereço de entrega que consta em nosso cadastro "
                f"é {endereco_formatado}. Caso o mesmo não corresponda solicitamos que entre em sua conta pessoal e atualizar o seu cadastro.")

    print(f"\033[32;40m{mensagem}\033[m")

    # Enviar e-mail
    enviar_email(email, "Confirmação de Pedido", mensagem)