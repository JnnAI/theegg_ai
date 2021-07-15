import time

def suma_lineal(n):
    suma=0
    for i in range(n+1):
        if i<=1:
            suma=i+i
        else:
            suma=suma+i
    return suma-1


def suma_constante(n):
    suma=int((n/2)*(n+1))
    return suma


cantidad=1000000

for i in range(4):
    t0=time.time()
    suma1=suma_lineal(cantidad)
    t1=time.time()
    suma2=suma_constante(cantidad)
    t2=time.time()

    print("{}  -  {}".format(suma1, t1-t0))
    print("{}  -  {}".format(suma2, t2-t1))
    print("\n")

    cantidad=cantidad*10