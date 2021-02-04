#Author: Társis Natan Boff da Silva"
#04/02/2021

import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import jsonlines

class WepscrpCorreios():

    #inputs
    btn_buscar_path = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/form/div/div/div[4]/input'

    btn_prox_path = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]'
    btn_nov_busca_path = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]'
    #outputs
    table_first_path= '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table[2]'
    table_path = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table'

    UF_list = ["AC","AL","AM","AP","BA","CE","DF", 
                "ES","GO","MA","MG","MS","MT", 
                "PA","PB","PE","PI","PR","RJ", 
                "RN", "RO", "RS","SC","SE","SP","TO"]

    def __init__(self):
        self.browser = self.setup_browser()
        
    def run(self):
        for indx, uf in enumerate(self.UF_list):
            #go to url base
            self.uf_acess_data(uf)
            #get data 
            uf_records = self.uf_get_data_records()
            #save in JSONL
            self.dump_file_json(uf_records, uf)
        self.close_browser()

    def uf_acess_data(self, uf):
        print(uf)
        self.browser.get('http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm')
        self.estados = Select(self.browser.find_element_by_name('UF'))
        self.estados.select_by_visible_text(uf)
        btn_nov_busca = self.browser.find_element_by_xpath(self.btn_buscar_path)
        btn_nov_busca.click()

    def uf_get_data_records(self):
        element = self.browser.find_element_by_xpath(self.table_first_path)
        all_frames = []
        id_cont = 0
        while(True):    
            df = self.generate_data_frame(element, id_cont) 
            id_cont += len(df)
            all_frames.extend(df.to_dict('records'))    

            if self.check_prox_page() == True:
                print("next")
                prox = self.browser.find_element_by_xpath(self.btn_prox_path)
                prox.click()
                element = self.browser.find_element_by_xpath(self.table_path)
            else: 
                print("stop")
                nova_busca = self.browser.find_element_by_xpath(self.btn_nov_busca_path)
                nova_busca.click()
                break
        print(all_frames)
        return all_frames
    
    def generate_data_frame(self, html_element, id_cont):   
        html = html_element.get_attribute('outerHTML')
        self.soup = BeautifulSoup(html, 'html.parser')
        table = self.soup.find(name='table')
        data_frame_full = pd.read_html(str(table))[0].head(50)
        data_frame = data_frame_full[["Localidade", "Faixa de CEP"]]
        id_column = self.generate_id(id_cont,data_frame)
        data_frame.insert(0, "ID", id_column)
        return data_frame

    def generate_id(self, id_cont, data_frame): 
        id_column = []
        for i  in range (0, len(data_frame)):
            id_cont += 1
            id_column.append(id_cont)         
        return id_column

    def dump_file_json(self, records, file_name):
        with jsonlines.open(file_name, 'w') as writer:
            writer.write_all(records)
            
    def check_prox_page(self): 
        prox = self.browser.find_element_by_xpath(self.btn_prox_path)
        a = prox.find_elements_by_tag_name('a') 
        if(a != []):
            checker = True
        else: 
            checker = False
        return checker  

    def setup_browser(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": 2})

        browser = webdriver.Chrome(chrome_options=chrome_options)
        return browser

    def close_browser(self): 
        self.browser.close

if __name__ == '__main__':

    web_scrpy = WepscrpCorreios()

    web_scrpy.run()

    print("All records was stored.")


