'''
Implementa el problema del productor-consumidor utilizando hilos,
donde un hilo produce datos y otro hilo los consume desde una cola
compartida
'''

from threading import Thread
from collections import deque
import time

def productor(cola):
    i = 1
    while True:
        time.sleep(1)
        if len(cola) >= 5:
            i = 0
            continue
        cola.append(i)
        print(f"Se agrego producto {i}")
        i+=1

def consumidor(cola):
    while True:
        time.sleep(1)
        if len(cola) == 0:
            print("No hay productos para consumir")
            continue
        x = cola.popleft()
        print(f"Se consumio producto {x}")


cola = deque()

Thread(target=productor, args=(cola,)).start()
Thread(target=consumidor, args=(cola,)).start()
