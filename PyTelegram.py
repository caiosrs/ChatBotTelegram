import telebot

with open(r'D:\1Desktop\Documentos\My Web Sites\App py\ChatBot Chamados\token telegram.txt', 'r') as file:
    token = file.read().strip()

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    chamado="""
    "Por favor, informe a categoria desejada:"
        /tecnico - Para manunteção de máquinas.
        /acessos - Para alterações e criação de acessos.
        /instalacoes - Para instalação de aplicativos/certificado.

        /outros - Para nenhuma dessas opções acima.
"""

    bot.reply_to(mensagem, chamado)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.reply_to(mensagem, "O ChamadosInfo_Bot de Triagem de Chamados é uma ferramenta de assistência que facilita a entrada de solicitações ao direcionar usuários para o atendimento adequado. Com uma interação amigável, ele tria e encaminha os chamados de forma eficiente, simplificando o processo para os atendentes e proporcionando uma experiência mais fluida para os usuários. Feito para a InformatecServiços.")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    pass

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção a seguir (Clique no item):
        /opcao1 - Abrir Chamado.
        /opcao2 - Saber mais.
        /opcao3 - Sair!

    Qualquer outra coisa não vai funcionar, clique em uma das opções a cima!
    """
    bot.reply_to(mensagem, texto)

bot.polling()