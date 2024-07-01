from conectorDB import conectar_banco_de_dados, fechar_conexao
from consultarEMAIL import pegar_EMAIL
from datetime import datetime, timedelta

def consulta_banco():
    resultados_consulta = []
    
    conexao = conectar_banco_de_dados('zabbix')
    if conexao:
        try:
            cursor = conexao.cursor()

            consulta = ("SELECT * FROM incidente_view WHERE `Tempo Down` > '00:20:00';")

            cursor.execute(consulta)

            resultados = cursor.fetchall()

            for resultado in resultados:
                # Atribua cada coluna a uma variável
                nome_biblioteca = resultado[0]
                data = resultado[1]
                tempo_queda = resultado[2]

                resultados_consulta.append([nome_biblioteca, data, tempo_queda])
            
            print(resultados_consulta, '\n')

        except Exception as erro:
            print("Erro: ", erro)

        finally:
            cursor.close()
            fechar_conexao(conexao)

    return resultados_consulta


def consulta_chamados_ativos():
    resultados_consulta = []
    
    email_dict = pegar_EMAIL()

    lista_nome_bibliotecas = []
    lista_nome_chamados = []
    for nome in email_dict.keys():
        lista_nome_bibliotecas.append(nome)
        lista_nome_chamados.append(f'Queda de internet na {nome}')

    conexao = conectar_banco_de_dados('tihdteste')
    if conexao:
        try:
            cursor = conexao.cursor()
            for nome_chamado, nome_biblioteca in zip(lista_nome_chamados, lista_nome_bibliotecas):
                consulta = (f"SELECT id, name, status FROM glpi_tickets WHERE name = %s AND status = 1;")
                cursor.execute(consulta, (nome_chamado,))

                resultados = cursor.fetchall() 

                if resultados:
                    resultados_consulta.append(nome_biblioteca)

            print(resultados_consulta, '\n')
            
            if resultados_consulta:
                return resultados_consulta
            else:
                return ''
        except Exception as erro:
            print("Erro: ", erro)

        finally:
            cursor.close()
            fechar_conexao(conexao)


def insercao_banco(nome_biblioteca):

    conexao = conectar_banco_de_dados('tihdteste')
    if conexao:

        data_atual = datetime.now()
        data_atual = data_atual.strftime('%Y-%m-%d %H:%M:%S')

        try:
            cursor = conexao.cursor()

            comando = (f"INSERT INTO glpi_tickets (name, date) VALUES (%s, %s);")
            valores = (f'Queda de internet na {nome_biblioteca}', f'{data_atual}')

            cursor.execute(comando, valores)

            conexao.commit()

            print('Dados inseridos!\n')

        except Exception as erro:
            print("Erro: ", erro)

        finally:
            cursor.close()
            fechar_conexao(conexao)
