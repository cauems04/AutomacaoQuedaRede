import win32com.client as win32
from consultasDB import consultaBanco
import re

outlook = win32.Dispatch('outlook.application')

def escrever_email(outlook, dest, assunto, corpo):

    try:

        email = outlook.CreateItem(0)

        email.To = dest
        email.Subject = assunto
        email.Body = corpo

        email.Send()
        print('Email enviado para: ', dest, 'com sucesso!')

    except Exception as e:
        print('Erro: ', e)


def enviar_mensagens_internet():

    dados = consultaBanco()
        
    if dados:

        for dado in dados:

            if dado[0].startswith('Biblioteca'):

                dest = 'espaguetecomalmondega00@gmail.com'
                assunto = f'Queda de rede na {dado[0]}'
                corpo = f'Olá, aqui é o Cauê, falando diretamente da CSMB, gostaria de informar que a rede da {dado[0]} está ausente e precisa de suporte.\nHorário da queda: {dado[1]}\n\nObrigado pela atenção.\n\n*Esta é uma mensagem automática*\nFavor *NÃO* responder.'

                escrever_email(outlook, dest, assunto, corpo)

            else:
                print(f'Conjunto de dados do {dado[0]} não pertencem a uma biblioteca.')
    else:
        print('Não há presença de dados.')


enviar_mensagens_internet()






























