'''
Lee un archivo CSV que contiene registros de datos y realiza alguna
operación de procesamiento en los datos, cómo calcular promedios,
encontrar valores máximos o mínimos, o filtrar registros que cumplan
ciertas condiciones.
'''

import csv

def salary_media(dict):
    media = 0
    for i in dict:
        media += int(i["salario"])
    return media / len(dict)

def max_salary(dict):
    maxs = max(x["salario"] for x in dict)
    return maxs

def min_salary(dict):
    mins = min(x["salario"] for x in dict)
    return mins

with open('whatever.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = []
    for i in reader:
        data.append(i)    

    maxs = max_salary(data.copy())
    mins = min_salary(data.copy())
    media = salary_media(data.copy())

    print(maxs,mins,media)
