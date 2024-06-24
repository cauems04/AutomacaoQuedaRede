import pandas as pd

def pegarEMAIL():
    try:
        df_geral = pd.read_excel("c:\\Users\\x561956\\OneDrive - rede.sp\\Documentos\\AutomacaoQuedaRede\\nome_email_bibliotecas.xlsx")
        email_dict = {}
        for index, linha in df_geral.iterrows():
            local = linha["Nome"]
            email = linha["E-mail"]
            email_dict[local] = email
        return email_dict
    except Exception as e:
        print(f"Erro ao ler o arquivo Excel: {e}")
        return None
