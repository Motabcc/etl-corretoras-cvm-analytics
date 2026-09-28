import requests
import pandas as pd
from sqlalchemy import create_engine

print("Iniciando extração de dados das Corretoras (CVM)...")
url_cvm = "https://brasilapi.com.br/api/cvm/corretoras/v1"
response = requests.get(url_cvm)

if response.status_code == 200:

    db_url = "postgresql+psycopg2://postgres.jmacxymmuejokmfszohu:SENHA@aws-0-us-west-2.pooler.supabase.com:PORTA/postgres"
    engine = create_engine(db_url)
    
    dados_cvm = response.json()
    df_cvm = pd.DataFrame(dados_cvm)
    
    # Tratamentos dos dados
    df_cvm['data_registro'] = pd.to_datetime(df_cvm['data_registro'], errors='coerce')
    df_cvm['ano_registro'] = df_cvm['data_registro'].dt.year
    df_cvm['mes_registro'] = df_cvm['data_registro'].dt.month
    df_cvm['valor_patrimonio_liquido'] = pd.to_numeric(df_cvm['valor_patrimonio_liquido'], errors='coerce').fillna(0)

    print(df_cvm[['nome_social', 'ano_registro', 'valor_patrimonio_liquido']].head())
    
    df_cvm.to_csv("corretoras_cvm.csv", index=False)
    print("\nSucesso! Arquivo 'corretoras_cvm.csv' salvo na pasta.")
    
    # Envia para o Supabase via conexão direta
    df_cvm.to_sql("corretoras_cvm", engine, if_exists="replace", index=False)
    print("Sucesso! Tabela criada e dados enviados para o Supabase.")

else:
    print("Erro: ", response.status_code)
    print("Não foi possível extrair os dados")