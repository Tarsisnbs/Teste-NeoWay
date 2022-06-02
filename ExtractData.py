from bs4 import BeautifulSoup

input_html = '' 


def parse_html(input_html):
    return BeautifulSoup(input_html, 'html.parser').prettify()

def search_all_urls(soup_html:BeautifulSoup): 
    for link in soup_html.find_all('a'):
        print(link.get('href'))
        
def framing_table(soup_html:BeautifulSoup): 
    return soup_html.find(name='table')
    
