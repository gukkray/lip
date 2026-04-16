import time
contador = 10

while(contador > 0):

    if (contador == 1):
        print(contador)
        break

    print(contador, end=', ', flush=True)
    contador = contador- 1
    time.sleep(1)
