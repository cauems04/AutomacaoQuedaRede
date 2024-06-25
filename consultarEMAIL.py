import pandas as pd

def pegarEMAIL():

    email_dict = {}
    try:
        df_geral = pd.read_excel("c:\\Users\\x540865\\Documents\AutomacaoQuedaRede\\nome_email_bibliotecas.xlsx")
        for index, linha in df_geral.iterrows():
            local = linha["Nome"]
            email = linha["E-mail"]
            email_dict[local] = email
    
        return email_dict
    except Exception as e:
        print(f"Erro ao ler o arquivo Excel: {e}")
        return None

pegarEMAIL()