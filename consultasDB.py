from conectorDB import conectar_banco_de_dados, fechar_conexao

def consultaBanco():
    resultados_consulta = []
    
    conexao = conectar_banco_de_dados()
    if conexao:
        try:
            cursor = conexao.cursor()

            consulta = ("SELECT * FROM incidente_view WHERE 'Tempo Down' > '00:20:00'")

            cursor.execute(consulta)

            resultados = cursor.fetchall()

            for resultado in resultados:
                # Atribua cada coluna a uma variável
                nome_biblioteca = str(resultado[0])
                data = resultado[1]
                tempo_queda = resultado[2]

                resultados_consulta.append([nome_biblioteca, data, tempo_queda])

        except Exception as erro:
            print("Erro: ", erro)

        finally:
            cursor.close()
            fechar_conexao(conexao)

    return resultados_consulta
