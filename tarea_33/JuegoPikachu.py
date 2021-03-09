
#AQUI ESTA EL PROGRAMA HECHO DE FORMA LINEAL, SIN FUNCIONES NI CLASES.

'''
psPika=100
psJig=100
atqPika=55
atqJig=45

Turno=1

while (psPika>0 and psJig>0):
    if Turno==1:
        psPika=psPika-atqJig
        Turno=0

    else:
        psJig=psJig-atqPika
        Turno=1


if psPika<=0:
    print('Gana Jigglipuff')
else:
    print('Gana Pikachu')
    
'''


#AQUI EMPIEZA EL PROGRAMA HECHO CON CLASES

class pokemon:

    def __init__(self, v, a):
        self.vida = v
        self.ataque = a

    
    def atacar(self, pokemon):
        pokemon.vida = pokemon.vida - self.ataque


pikachu=pokemon(100, 55)
jigglypuff=pokemon(100, 45)

Turno=1

while (pikachu.vida>0 and jigglypuff.vida>0):
    if Turno==1:
        print('Jigglypuff ataca a Pikachu')
        jigglypuff.atacar(pikachu)
        Turno=0

    else:
        print('Pikachu ataca a Jigglypuff')
        pikachu.atacar(jigglypuff)
        Turno=1


if pikachu.vida<=0:
    print('Gana Jigglypuff')
else:
    print('Gana Pikachu')