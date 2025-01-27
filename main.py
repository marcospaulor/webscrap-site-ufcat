import json
import requests
import time
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicialize o aplicativo Firebase
cred = credentials.Certificate("./database/servicos-ufcat-app-firebase-adminsdk-wf4o4-7becca3684.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://servicos-ufcat-app-default-rtdb.firebaseio.com/'
})

# Referência para o banco de dados Firebase
ref = db.reference('/')

class WebScrap:
    def __init__(self):
        self.urls = {
            "noticia": "https://ufcat.edu.br/noticias",
            "evento": "https://ufcat.edu.br/eventos",
            "edital": "https://ufcat.edu.br/editais"
        }

        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')  # Execute o navegador em segundo plano (sem janela)
        self.driver = webdriver.Chrome(options=options)  # Certifique-se de ter o WebDriver do Chrome configurado corretamente

    def _extract_data(self, url, data_type):
        data_list = []

        self.driver.get(url)
        time.sleep(2) # Espera 2 segundos para a página carregar

        while True:
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            tile_items = soup.select('.tileItem')

            for tile_item in tile_items:
                link = tile_item.select_one('a')['href']
                title = tile_item.select_one('.tileHeadLine').get_text(strip=True)
                image_element = tile_item.select_one('img')
                image_url = image_element['src'] if image_element else ''
                alt_text = image_element['alt'] if image_element else ''
                date_element = tile_item.select_one('.tileDateNews') or tile_item.select_one('.tileDate span')
                date = ' '.join(date_element.stripped_strings) if date_element else ''

                data_list.append({
                    'type': data_type,
                    'link': link,
                    'title': title,
                    'date': date,
                    'image_url': image_url,
                    'alt_text': alt_text
                })

            next_button = self.driver.find_element(By.CSS_SELECTOR, '[data-next-page="data-next-page"]')
            # Encontre a tag <nav>
            nav_element = self.driver.find_element(By.CSS_SELECTOR, 'nav[data-total][data-current]')

            
            # Extraia os valores dos atributos data-current e data-total
            data_current_str = nav_element.get_attribute('data-current')
            data_total_str = nav_element.get_attribute('data-total')
            
            # Verifique se ambos os valores não são None
            if data_current_str is None or data_total_str is None:
                print("Um dos atributos data-current ou data-total é None. Parando o scraping.")
                break
            
            # Converta os valores para inteiros
            data_current = int(data_current_str)
            data_total = int(data_total_str)
            
            # Verifique se a condição de parada é atendida
            if data_current == data_total:
                print("Chegou ao fim das páginas. Parando o scraping.")
                break
            else:
                self.driver.execute_script("arguments[0].click();", next_button)
                time.sleep(2) # Espera 2 segundos para a próxima página carregar

        return data_list

    def scrape_and_save(self):
        all_data = []
        for data_type, url in self.urls.items():
            data = self._extract_data(url, data_type)
            all_data.extend(data)

        ref.child('data').set(all_data)
        print("Dados salvos com sucesso no Firebase!")

    def read_data_from_firebase(self):
        data = ref.child('data').get()
        if data:
            return data
        else:
            print("Nenhum dado encontrado no Firebase.")
            return []

    def quit_driver(self):
        self.driver.quit()

# Usando a classe WebScrap
web_scrap = WebScrap()
web_scrap.scrape_and_save()
web_scrap.quit_driver()