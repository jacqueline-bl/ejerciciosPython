#Programa
print('PROGRAMA: Verificar si una palabra es un anagrama de otra')
#Variables
palabra1=str(input('Escriba una palabra en minúsculas:'))
palabra2=str(input('Escriba otra palabra en minúsculas:'))
#Algoritmo
palabraInvertida = palabra2[::-1]
if palabra1==palabraInvertida:
    print  (f'La palabra {palabra2} es un anagrama de la palabra {palabra1}')
else:
    print  (f'La palabra {palabra2} no es un anagrama de la palabra {palabra1}')
#Fin
