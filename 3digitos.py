#Programa
print('PROGRAMA: Verificar si una cadena de texto contiene solo dígitos.')
#Variables
cadena= (input('Ingrese una cadena de carácteres desde su teclado:'))
#Algoritmo

if cadena.isdigit():
    print(f'La cadena {cadena}, contiene solo dígitos; es decir, números enteros positivos.')
else:
    print(f'La cadena: {cadena}, contiene letras.')
#Fin