'''
Crea dos hilos que ejecuten dos funciones diferentes simultáneamente
y muestran mensajes de salida
'''

import threading

def count_25():
    for i in range(26):
        print(f"Primer Thread, valor: {i}\n")

def count_50():
    for i in range(26,51):
        print(f"Segundo Thread, valor {i}\n")

threading.Thread(target=count_25, daemon=True).start()
threading.Thread(target=count_50, daemon=True).start()
