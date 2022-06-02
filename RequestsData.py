
from matplotlib.pyplot import table
import requests
from bs4 import BeautifulSoup


url_is = ' https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'
n_linhas = 100
index_ini = 1
UF_list = ["AC","AL","AM","AP","BA","CE","DF", 
            "ES","GO","MA","MG","MS","MT", 
            "PA","PB","PE","PI","PR","RJ",
               "RN", "RO", "RS","SC","SE","SP","TO"]
uf = 0
formulario = {
    'UF': UF_list[uf],
    'Localidade': '**',
    'Bairro': '',
    'qtdrow': str(n_linhas),
    'pagini': str(index_ini),
    'pagfim': str(index_ini + n_linhas),
}

requisition = requests.post(url_is,data=formulario)
#print(requisition.headers)
#print((requisition.content), 'html.parser')
print("url:", requisition.url)
print("headers:", requisition.headers)