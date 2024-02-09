'''
Utiliza un pool de procesos para realizar operaciones en paralelo en
una lista de datos
'''

from multiprocessing import Pool


def sumar(n):
    return n+n

lista = [1,2,3,4,5]

if __name__ == '__main__':
    with Pool(3) as p:
        print(p.map(sumar, lista))
