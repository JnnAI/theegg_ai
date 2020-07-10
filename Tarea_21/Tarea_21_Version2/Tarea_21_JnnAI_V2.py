
numero = 0
while True:
   
    try:
        numero = float(input('Introduce un numero comprendido entre 0.0001 y 0.9999 por favor: '))
    except ValueError:
        print('El valor introducido debe ser un número')
        
  
    if (numero >= 0.0001 and numero <= 0.9999):
        break


    elif (numero<=0.0001 and numero >=0.9999): 
        print("El valor que has introducido es incorrecto.")



print('Número correcto.')


numerador = int(numero*10000)
denominador = 10000

contador = 1

while contador <= numerador:
    if numerador % contador == 0 and denominador % contador == 0:
        num = int(numerador / contador)
        den = int(denominador / contador)
    contador = contador + 1



print(f'La fraccion reducida de ese numero es:{num} / {den}')
 
        





    
  