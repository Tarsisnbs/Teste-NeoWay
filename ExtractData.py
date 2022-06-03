from bs4 import BeautifulSoup

input_html = '' 


def parse_html(input_html):
    return BeautifulSoup(input_html, 'html.parser').prettify()

def search_all_urls(soup_html:BeautifulSoup): 
    for link in soup_html.find_all('a'):
        print(link.get('href'))
        
def get_table_from_text(html_txt:str): 
    return BeautifulSoup(html_txt, 'html.parser').find_all(name='table')

    
