from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3
import time

def get_weather_info_selenium(url):
    """
    Função para capturar informações do clima usando Selenium.
    """
    try:
        # Configuração do navegador
        service = FirefoxService()
        driver = webdriver.Firefox(service=service)

        # Acessar o site
        driver.get(url)
        driver.maximize_window()

        # Aguardar carregamento dos elementos principais
        wait = WebDriverWait(driver, 10)
        title_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title-h1")))
        temp_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dato-temperatura")))
        condition_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "descripcion")))

        # Extrair os dados
        weather_info = {
            "Região": title_element.text.strip(),
            "Temperatura": temp_element.text.strip(),
            "Condição": condition_element.text.strip()
        }

        print("Dados obtidos com sucesso!")
        return weather_info

    except Exception as e:
        return {"Erro": f"Erro ao coletar dados com Selenium: {e}"}

    finally:
        # Garantir que o navegador seja fechado
        driver.quit()

def save_to_database(weather_info):
    """
    Salva as informações do clima no banco de dados SQLite.
    """
    try:
        connection = sqlite3.connect('weather_data.db')
        cursor = connection.cursor()

        # Criar tabela se não existir
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            region TEXT NOT NULL,
            temperature TEXT NOT NULL,
            condition TEXT NOT NULL
        )
        ''')

        if "Erro" in weather_info:
            print(f"Erro ao salvar dados: {weather_info['Erro']}")
            return

        # Inserir dados no banco
        cursor.execute('''
        INSERT INTO weather_data (region, temperature, condition) 
        VALUES (?, ?, ?)
        ''', (
            weather_info['Região'], 
            weather_info['Temperatura'], 
            weather_info['Condição']
        ))
        connection.commit()

        print("Dados salvos com sucesso no banco de dados!")

    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")
    finally:
        if connection:
            connection.close()

# URL da página
url = "https://www.tempo.com/sao-paulo.htm"

# Obter informações meteorológicas com Selenium
weather_info = get_weather_info_selenium(url)

# Exibir informações coletadas
for key, value in weather_info.items():
    print(f"{key}: {value}")

# Salvar no banco de dados
save_to_database(weather_info)
