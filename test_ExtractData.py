import RequestsData as rd
import ExtractData as ed
import codecs
from bs4 import BeautifulSoup

from bs4 import BeautifulSoup
test_path = 'test_files/'
file_in = 'request_response.txt'
file_out = 'table_html.html'
import codecs

with open(test_path + file_in, 'r') as f:
    html_txt = (f.read())

html_parsed = ed.parse_html(html_txt) 

html_tables = ed.get_table_from_text(html_parsed)

if (len(html_tables[0]) == 5):
    html_table = html_tables[1]
else:
    html_table = html_tables[0]
    
with open(test_path + file_out, "w") as f:
     f.write(str(html_table))
     
