'''
Lee un archivo CSV que contiene registros de datos y convertirlo en un
archivo JSON.
'''

import csv
import json

with open('whatever.csv', 'r') as f:
    csv_data = csv.DictReader(f)
    data = []
    for i in csv_data:
        data.append(i)
    json_format = json.dumps(data)
    print(json_format)