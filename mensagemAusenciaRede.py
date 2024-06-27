import win32com.client as win32
import schedule
from consultasDB import consultaBanco, insercaoBanco, consultaChamadosAtivos
from consultarEMAIL import pegarEMAIL

outlook = win32.Dispatch('outlook.application')

def escrever_email(outlook, dest, assunto, corpo, nome_biblioteca):

    try:

        email = outlook.CreateItem(0)
        email.To = dest
        email.Subject = assunto
        email.Body = corpo
        email.Send()
        print(f'\nEmail enviado para: {dest} com sucesso!({nome_biblioteca})')

    except Exception as e:
        print('Erro ao enviar email: ', e)


def enviar_mensagens_internet():

    bibliotecas_chamados_ativos = consultaChamadosAtivos()
    dados = consultaBanco()
    email_dict = pegarEMAIL()
        
    if email_dict is None:
        print("Erro ao obter emails. Verifique o arquivo Excel.")
        return

    try:

        if dados:

            for dado in dados:
                nome_biblioteca = dado[0]

                if nome_biblioteca.startswith('Biblioteca'):
                        
                    if nome_biblioteca in email_dict:
                            
                        if nome_biblioteca not in bibliotecas_chamados_ativos:
                            dest = 'lseloy@prefeitura.sp.gov.br'
                            assunto = f'Queda de rede na {nome_biblioteca}'
                            corpo = (f'Ola, Nosso sistema de monitoramento identificou uma queda na rede de internet da {nome_biblioteca}, a queda ocorreu em {dado[1]}.\n\nDesde já, a cordenadoria do sistema municipal de bibliotecas agradece.')
                                    
                            escrever_email(outlook, dest, assunto, corpo, nome_biblioteca)
                            insercaoBanco(nome_biblioteca)

                            dest = email_dict[nome_biblioteca]
                            assunto = f'Queda de rede na {nome_biblioteca}'
                            corpo = (f'Olá, aqui é a equipe de TI, gostaria de informar que a {nome_biblioteca} está sem rede de internet, já foi aberto um chamado para reparo e manutenção.\n'
                                        f'Horário da queda: {dado[1]}\n\nObrigado pela atenção.\n\n*Esta é uma mensagem automática*\nFavor *NÃO* responder.')
                                    
                            escrever_email(outlook, dest, assunto, corpo, nome_biblioteca)

                        else:
                            print(f'Já existe um chamado ativo para a {nome_biblioteca}.\n')
                            
                    else:
                        print(f'Email para {nome_biblioteca} não encontrado na planilha.\n')

                else:
                    print(f'Conjunto de dados do {dado[0]} não pertence a uma biblioteca.\n')

        else:
            print('Não há presença de dados.\n\n')
        
        print('----------------')
    
    except Exception as e:
        print('Erro :', e)

schedule.every(10).minutes.do(enviar_mensagens_internet)

while True:
    schedule.run_pending()