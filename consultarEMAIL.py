import pandas as pd





def pegarEMAIL():
    df_geral = pd.read_excel("c:\\Users\\x561956\\OneDrive - rede.sp\\Documentos\\AutomacaoQuedaRede\\nome_email_bibliotecas.xlsx")
    for index, linha in df_geral.iterrows():


        local = linha["Nome"]
        data = linha["E-mail"]

        print(local, data)

pegarEMAIL()        