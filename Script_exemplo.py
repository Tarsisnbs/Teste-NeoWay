import RequestsData as rd
import ExtractData as ed
import CleanData as cd

path = 'uf_files/'


url_is = ' https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'
n_linhas = 100
'''
UF_list2 = [("AC", 24),("AL", 107),("AM", 68),("AP", 19),("BA", 438),("CE", 200),("DF", 5), 
            ("ES", 90),("GO", 269),("MA", 224),("MG", 924),("MS", 85),("MT", 150), 
            ("PA", 158),("PB", 231),("PE", 205),("PI", 229),("PR", 433),("RJ", 130),
               ("RN", 173), ("RO", 58), ("RO", 17), ("RS", 535),("SC", 322),("SE", ),("SP", 874),("TO", 143)]
'''

UF_list = ["AC","AL","AM","AP","BA","DF", 
                "ES","GO","MA","MG","MS","MT", 
                "PA","PB","PE","PI","PR","RJ", 
                "RN", "RO", "RS","SC","SE","SP","TO"]


def run_script():
        uf = 0
        for indx, uf in enumerate(UF_list):
            row_ini = 1
            id_cnt = 0
            file_out = uf
            
            while(id_cnt + 1 >= row_ini):                       # verifica a ocorrencia da última linha da tabela para a uf indexada
                print((uf))
                form = refresh_form(uf, row_ini)
                request = rd.do_request(url_is, form) 
                
                html_parsed = ed.parse_html(request['text']) 
                html_tables = ed.get_table_from_text(html_parsed)
                if (len(html_tables[0]) == 5):
                    html_table = html_tables[1]
                else:
                    html_table = html_tables[0]
                frame = cd.generate_data_frame(str(html_table), id_cnt)
            
                cd.dump_file_json(frame.to_dict('records'), path + file_out)
 
                id_cnt += len(frame)
                row_ini += 100
                       
        print("done.")
            
def refresh_form(uf, index_ini):
    form = {
        'UF': uf,
        'Localidade': '**',
        'Bairro': '',
        'qtdrow': str(n_linhas), #global
        'pagini': str(index_ini),
        'pagfim': str(index_ini + n_linhas),
    }
    
    return form



if __name__ == "__main__":
    run_script()