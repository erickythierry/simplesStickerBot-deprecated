import time
from src import WhatsAPIDriver
from src.objects.message import Message

driver = WhatsAPIDriver(client='chrome', profile='./arquivos/usuario')
print("esperando leitura do codigo QR")
while not driver.wait_for_login():
    time.sleep(3)

print("Bot inciado")

while True:
	time.sleep(1)
	for contact in driver.get_unread():
		for message in contact.messages:
			if isinstance(message, Message):
				
				
				tipoMsg = message.type # tipo de mensagem: imagem, video, texto, Sticker, etc...
				idChat = message.chat_id # id do chat que mandou a mensagem. ex: 5511223344@c.us
				idSender = message.sender # id de quem mandou a mensagem. se for mensagem de um grupo, o idChat será diferente do idSender 

				if tipoMsg == "image":
					print(f'recebi uma imagem de {idChat}')
					nomeArquivo = message.save_media("./arquivos/imagens", force_download=True) # as fotos recebidas são salvas na pasta imagens
					driver.send_image_as_sticker(f'./arquivos/imagens/{nomeArquivo}', idChat) # a foto recebida é enviada como figurinha
				
				elif tipoMsg == "chat":
					print(f'recebi uma mensagem de {idChat}')
					contact.chat.send_message('ola, sou um Robô, me mande uma foto e veja oq acontece :)')

				
				
