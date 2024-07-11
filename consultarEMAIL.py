import pandas as pd

def pegar_EMAIL():

    email_dict = {}
    try:
        df_geral = pd.read_excel("c:\\Users\\x540865\\Documents\AutomacaoQuedaRede\\BibliotecasNomesEmailsIDs.xlsx")
        for index, linha in df_geral.iterrows():
            local = linha["Nome"]
            email = linha["E-mail"]
            id = linha["ID"]
            email_dict[local] = [email, id]

        return email_dict
    except Exception as e:
        print(f"Erro ao ler o arquivo Excel: {e}")
        return None