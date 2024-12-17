# Processo de ETL: Extração, Transformação e Load de Dados da Tempo.com para o Banco de Dados

Este projeto realiza um processo **ETL (Extração, Transformação e Load)** para capturar dados meteorológicos do site da Tempo (https://www.tempo.com/) utilizando **Selenium**. As informações extraídas são armazenadas em um banco de dados **SQLite**.

---

## **Funcionalidades do Script**

1. **Extração de Dados**:
   - Acessa automaticamente o site de previsão do tempo utilizando **Selenium**.
   - Extrai:
     - **Região** da previsão.
     - **Temperatura** atual.
     - **Condição do tempo** (ex.: ensolarado, nublado, etc.).

2. **Transformação de Dados**:
   - Organiza os dados coletados em um formato estruturado.

3. **Armazenamento dos Dados**:
   - Salva os dados em um banco de dados **SQLite** na tabela `weather_data`.

---

## **Bibliotecas Utilizadas**

- **Selenium**: Automação da navegação web e coleta de dados.
- **sqlite3**: Criação e gerenciamento do banco de dados SQLite.
- **time**: Controle de temporização no script.

---
