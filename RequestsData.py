
from tokenize import String
from matplotlib.pyplot import table
import requests
from bs4 import BeautifulSoup


def do_request(url_is:String, form:dict):

    requisition = requests.post(url_is,data=form)
    
    return {'status': requisition.status_code, 'url': requisition.url,  'text': requisition.text, 'content': requisition.content}