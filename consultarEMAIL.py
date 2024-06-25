import pandas as pd

def pegarEMAIL():
<<<<<<< HEAD
    try:
        df_geral = pd.read_excel("c:\\Users\\x561956\\OneDrive - rede.sp\\Documentos\\AutomacaoQuedaRede\\nome_email_bibliotecas.xlsx")
        email_dict = {}
=======

    email_dict = {}
    try:
        df_geral = pd.read_excel("c:\\Users\\x540865\\Documents\AutomacaoQuedaRede\\nome_email_bibliotecas.xlsx")
>>>>>>> main
        for index, linha in df_geral.iterrows():
            local = linha["Nome"]
            email = linha["E-mail"]
            email_dict[local] = email
<<<<<<< HEAD
=======
    
>>>>>>> main
        return email_dict
    except Exception as e:
        print(f"Erro ao ler o arquivo Excel: {e}")
        return None
<<<<<<< HEAD
=======

pegarEMAIL()
>>>>>>> main
