#Programa
print ('PROGRAMA: Calcular el perímetro de un cuadrado.')
#Variables
distanciaLado=float(input('Ingrese la distancia del lado del cuadrado, por ejemplo 8, 10.2, 15:'))
unidadLado= str(input('Ingrese la unidad de medida, por ejemplo cm, m, etc:'))
#Algoritmo
perimetroCuadrado= distanciaLado * 4 
#Fin 
print (f'El perímetro del cuadrado es {perimetroCuadrado} {unidadLado}')
