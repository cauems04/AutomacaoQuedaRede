import win32com.client as win32
from consultasDB import consultaBanco
from consultarEMAIL import pegarEMAIL

outlook = win32.Dispatch('outlook.application')

def escrever_email(outlook, dest, assunto, corpo):
    try:
        email = outlook.CreateItem(0)
        email.To = dest
        email.Subject = assunto
        email.Body = corpo
        email.Send()
        print('Email enviado para:', dest, 'com sucesso!')
    except Exception as e:
        print('Erro ao enviar email:', e)

def enviar_mensagens_internet():
    dados = consultaBanco()
    email_dict = pegarEMAIL()
    
    if email_dict is None:
        print("Erro ao obter emails. Verifique o arquivo Excel.")
        return
    
    if dados:
        for dado in dados:
            nome_biblioteca = dado[0]
            if nome_biblioteca in email_dict:
                dest = email_dict[nome_biblioteca]
                assunto = f'Queda de rede na {nome_biblioteca}'
                corpo = (f'Olá, aqui é o Cauê, falando diretamente da CSMB, gostaria de informar que a rede da {nome_biblioteca} está ausente e precisa de suporte.\n'
                         f'Horário da queda: {dado[1]}\n\nObrigado pela atenção.\n\n*Esta é uma mensagem automática*\nFavor *NÃO* responder.')
                escrever_email(outlook, dest, assunto, corpo)
            else:
                print(f'Email para {nome_biblioteca} não encontrado na planilha.')
    else:
        print('Não há presença de dados.')

enviar_mensagens_internet()
