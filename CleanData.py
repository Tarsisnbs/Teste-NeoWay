from bs4 import NavigableString, Tag
import pandas as pd
import jsonlines

def generate_data_frame(table_html, id_cont): 
    data_frame_full = pd.read_html(table_html)[0].head(100)
    data_frame = data_frame_full[["Localidade", "Faixa de CEP"]]
    id_column = generate_id(id_cont,data_frame)
    data_frame.insert(0, "ID", id_column)
    return data_frame
    

def generate_id(id_cont, data_frame): 
    id_column = []
    for i  in range (0, len(data_frame)):
        id_cont += 1
        id_column.append(id_cont)         
    return id_column

def dump_file_json(records, file_name):
    with jsonlines.open(file_name + '.jsonl', 'a') as writer:
        writer.write_all(records)