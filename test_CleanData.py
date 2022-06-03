import CleanData as cd
import jsonlines

test_path = 'test_files/'
file_in = 'table_html.html'
file_out = 'any_uf'
id_cont = 0

with open(test_path + file_in, 'r') as f:
    table = (f.read())
    
frame = cd.generate_data_frame(table, id_cont)

cd.dump_file_json(frame.to_dict('records'), test_path + file_out)


