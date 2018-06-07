###################################################################
# Exemplo de Envio de Email via Flask
# v1
# 28/05/2018
###################################################################
from flask import Flask, render_template
from flask_mail import Mail, Message
import yaml

app = Flask(__name__)

# Dados da caixa postal utilizada para enviar o email
emailbox = yaml.load(open('email_config.yaml'))
app.config['MAIL_SERVER']  			= emailbox['eserver']
app.config['MAIL_PORT']	 			= emailbox['port']
app.config['MAIL_USE_SSL']			= emailbox['protSSL']
app.config['MAIL_USE_TLS']  		= emailbox['protTLS']
app.config['MAIL_USERNAME'] 		= emailbox['username']
app.config['MAIL_PASSWORD'] 		= emailbox['password']
app.config['MAIL_DEFAULT_SENDER'] 	= emailbox['fromaddr'] 

mail = Mail(app) 

# Endereco de e-mail destino e mensagem que sera enviada
toaddrs = 'ademar.sigrist@gmail.com'
subject = 'E-mail Flask'
txt_msg = 'Mensagem de teste de envio de email via Flask'


# Página index.html
@app.route('/')
def index():
	msg = Message(subject, recipients=[toaddrs])
	#msg.body = txt_msg 
	msg.html = "<b>Esse e um teste de HTML</b>"
	#msg.html = render_template('body_curso_ml.html')
	#with app.open_resource("teste.txt") as fp:
	#	msg.attach("teste.txt", "text/plain", fp.read())
	with app.open_resource("Ficha_Resumo_ML_1.pdf") as fp:
		msg.attach("Ficha_Resumo_ML_1.pdf", "application/pdf", fp.read())
	try:
		mail.send(msg)
		return "<h1>E-mail e enviado com sucesso!  :) <h1>"
	except:
		return 'Ocorreu um ERRO no envio do E-mail!' 

if __name__ == '__main__':
	app.run(debug=True)  

