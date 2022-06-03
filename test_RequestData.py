import RequestsData as rd

test_path = 'test_files/'
url_is = ' https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'
n_linhas = 100
index_ini = 1 
UF_list = ["AC","AL","AM","AP","BA","CE","DF", 
            "ES","GO","MA","MG","MS","MT", 
            "PA","PB","PE","PI","PR","RJ",
               "RN", "RO", "RS","SC","SE","SP","TO"]
uf = 0
form = {
    'UF': UF_list[uf],
    'Localidade': '**',
    'Bairro': '',
    'qtdrow': str(n_linhas),
    'pagini': str(index_ini),
    'pagfim': str(index_ini + n_linhas),
}

request = rd.do_request(url_is, form) 

if request['status'] == 200: 
    print('request ok,')
    print('url:', request['url'])
    
    with open(test_path +'request_response.txt', "w") as f:
        f.write(request['text'])

    
else: 
    print("request fail!")