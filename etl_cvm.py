import requests
import pandas as pd

print("Iniciando extração de dados das Corretoras (CVM)...")
url_cvm = "https://brasilapi.com.br/api/cvm/corretoras/v1"
response = requests.get(url_cvm)

if response.status_code == 200:
    dados_cvm = response.json()
    
    # Estrutura em tabelas o nosso json
    df_cvm = pd.DataFrame(dados_cvm)
   
    # Agora podemos filtrar pelo tempo usando a data 
    df_cvm['data_registro'] = pd.to_datetime(df_cvm['data_registro'], errors='coerce')

    df_cvm['ano_registro'] = df_cvm['data_registro'].dt.year
    df_cvm['mes_registro'] = df_cvm['data_registro'].dt.month
    
    #pra ver o header: print(df_cvm.columns.tolist())
    
    # converter o patrimônio líquido para número decimal
    df_cvm['valor_patrimonio_liquido'] = pd.to_numeric(df_cvm['valor_patrimonio_liquido'], errors='coerce').fillna(0)

    #  amostra das colunas mais importantes
    print(df_cvm[['nome_social', 'ano_registro', 'valor_patrimonio_liquido']].head())
    
    df_cvm.to_csv("corretoras_cvm.csv", index=False)
    print("\nSucesso! Arquivo 'corretoras_cvm.csv' salvo na pasta.")
    
else:
    print("Erro: ", response.status_code)
    print("Não foi possível extrair os dados")