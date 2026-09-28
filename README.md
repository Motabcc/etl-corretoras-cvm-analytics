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
