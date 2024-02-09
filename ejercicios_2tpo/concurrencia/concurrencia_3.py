'''
Crea dos procesos utilizando la biblioteca multiprocessing y ejecuta
funciones diferentes en cada proceso.
'''

import multiprocessing

def count_25():
    for i in range(1,26):
        print(i)

def count_50():
    for i in range(26,51):
        print(i)

if __name__ == '__main__':
    p = multiprocessing.Process(target=count_25)
    p2 = multiprocessing.Process(target=count_50)
    p.start()
    p2.start()
    