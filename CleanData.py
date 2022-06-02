import pandas as pd

input_html = '' 

def generate_id(self, id_cont, data_frame): 
        id_column = []
        for i  in range (0, len(data_frame)):
            id_cont += 1
            id_column.append(id_cont)         
        return id_column