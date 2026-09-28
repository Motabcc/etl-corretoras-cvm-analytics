# 📊 Dashboard Corretoras CVM - ETL com Python no Power BI

Este projeto é um pipeline de ponta a ponta (End-to-End) que extrai dados públicos da CVM (Comissão de Valores Mobiliários), realiza a limpeza e transformação dos dados utilizando **Python**, e disponibiliza as métricas financeiras de forma automatizada no **Power BI**.

O grande diferencial deste projeto é a sua arquitetura de **Automação Nível 1**: o script de extração e tratamento roda nativamente dentro do motor do Power BI. Não há arquivos estáticos (como CSVs ou planilhas) intermediários. Ao clicar em "Atualizar" no painel, os dados mais recentes são puxados diretamente da API.

## 🛠️ Tecnologias Utilizadas
* **Fonte de Dados:** [Brasil API](https://brasilapi.com.br/) (Endpoint CVM)
* **Linguagem:** Python (Bibliotecas: `requests`, `pandas`)
* **Visualização e Orquestração:** Microsoft Power BI (Power Query Python Integration)

## 🏗️ Arquitetura e Modelagem
1. **Extração:** Conexão com o endpoint `https://brasilapi.com.br/api/cvm/corretoras/v1`.
2. **Transformação (Pandas):** 
   * Conversão de colunas de texto para formato `datetime` seguro, lidando com valores nulos.
   * Derivação de colunas temporais (`ano_registro`, `mes_registro`) para habilitar o uso de Inteligência de Tempo (DAX) no Power BI.
   * Tipagem de dados financeiros (`valor_patrimonio_liquido`) para formato decimal.
3. **Carga:** Ingestão do DataFrame `df_cvm` diretamente na memória do Power BI via script.

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o Python instalado na sua máquina e as bibliotecas necessárias:
```bash
pip install pandas requests
