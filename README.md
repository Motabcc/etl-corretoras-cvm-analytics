# 🚀 Pipeline de Dados CVM: De Script Local à Automação Cloud (ETL + n8n + Supabase + Power BI)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/n8n-Automation-orange?style=for-the-badge&logo=n8n&logoColor=white" />
  <img src="https://img.shields.io/badge/Supabase-Database-green?style=for-the-badge&logo=supabase&logoColor=white" />
  <img src="https://img.shields.io/badge/Power_BI-Analytics-yellow?style=for-the-badge&logo=powerbi&logoColor=white" />
</p>

---

## 🎯 Sobre o Projeto
Este repositório documenta a evolução prática de um projeto de **Engenharia e Integração de Dados**, estruturado em formato de **Monorepo**. O objetivo principal é consumir dados públicos de corretoras da **CVM (Comissão de Valores Mobiliários)** via API, tratá-los, persisti-los em um banco relacional em nuvem de forma automatizada e exibi-los em um dashboard analítico.

---

## 📈 Evolução da Arquitetura (Monorepo)
O projeto foi desenvolvido em fases para demonstrar a transição de um ambiente local e manual para uma arquitetura moderna orientada a microsserviços e automação:

```text
PROJETO-PIX/
├── docs/                     # Evidências, prints do fluxo e dashboard (.pbix)
├── v1-python-local/          # Fase 1: Script em Python e extração para CSV local
└── v2-automacao-n8n/         # Fase 2: Orquestração em nuvem com n8n e Supabase
```
🛠️ Detalhes das Fases
🔹 Fase 1: v1-python-local (Abordagem Tradicional)Objetivo: Prototipar a extração de dados consumindo a API da BrasilAPI (/api/cvm/corretoras/v1).   Tecnologias: Python, Pandas, Requests.Resultado: Limpeza inicial de datas, tratamento de campos numéricos (patrimônio líquido) e exportação para arquivo local (corretoras_cvm.csv).

🔹 Fase 2: v2-automacao-n8n (Arquitetura Cloud & Low-Code)Objetivo: Eliminar a dependência de execução manual e persistir os dados diretamente em um banco de dados relacional na nuvem.Orquestração: n8n configurado com um agendador (Schedule Trigger).   Persistência: Supabase (PostgreSQL) recebendo os dados limpos de forma automatizada (Upsert/Update via CNPJ).   Visualização: Power BI conectado diretamente à base em nuvem para consumo e geração de insights em tempo real.📊 Estrutura do Fluxo no n8nO fluxo automatizado de ETL segue a seguinte esteira de execução:   Schedule Trigger: Dispara a rotina automaticamente.   HTTP Request: Realiza a requisição GET na API da CVM.   Edit Fields (Set): Realiza o tratamento e formatação de datas e conversão de tipos numéricos.   Supabase Node: Conecta ao banco PostgreSQL e atualiza/insere os registros de forma segura[cite: 1, 2].O arquivo de configuração do fluxo exportado está disponível na pasta v2-automacao-n8n/workflow_cvm.json.📸 Evidências & DashboardNa pasta docs/, você encontrará:Prints do fluxo rodando no n8n (workflow_cvm.png).   
Estrutura de colunas da tabela no Supabase (columns_cvm.png).   
O arquivo do relatório do Power BI (Dashboard CVM.pbix).   
Feito com 💻 por Gabriel Sodré.
