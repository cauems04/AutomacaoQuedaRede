from conectorDB import conectar_banco_de_dados, fechar_conexao
from consultarEMAIL import pegarEMAIL
from datetime import datetime, timedelta

def consultaBanco():
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
            
            print(resultados_consulta)

        except Exception as erro:
            print("Erro: ", erro)

        finally:
            cursor.close()
            fechar_conexao(conexao)

    return resultados_consulta


def consultaChamadosAtivos():
    resultados_consulta = []
    
    email_dict = pegarEMAIL()

    lista_nome_chamados = []
    for nome in email_dict.keys():
        lista_nome_chamados.append(f'Queda de internet na {nome}')

    conexao = conectar_banco_de_dados('tihdteste')
    if conexao:
        try:
            cursor = conexao.cursor()
            for nome in lista_nome_chamados:
                consulta = (f"SELECT * FROM glpi_tickets WHERE name = {nome} AND status = 1;")
                cursor.execute(consulta)

                resultados = cursor.fetchall() 

                print(resultados)

        except Exception as erro:
            print("Erro: ", erro)

        finally:
            cursor.close()
            fechar_conexao(conexao)

consultaChamadosAtivos()


def insercaoBanco(nome_biblioteca):

    conexao = conectar_banco_de_dados('tihdteste')
    if conexao:

        data_atual = datetime.now()
        data_atual = data_atual.strftime('%Y-%m-%d %H:%M:%S')

        try:
            cursor = conexao.cursor()

            comando = (f"INSERT INTO glpi_tickets (name, date) VALUES ('Queda de internet na {nome_biblioteca}', '{data_atual}');")

            cursor.execute(comando)

            conexao.commit()

            print('Dados inseridos!')

        except Exception as erro:
            print("Erro: ", erro)

        finally:
            cursor.close()
            fechar_conexao(conexao)
