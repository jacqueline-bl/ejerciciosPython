#Programa
print('PROGRAMA: Invertir una lista de números')
#Variables
listaUsuario=(input('Ingrese una lista de números separados por comas:'))
#Algoritmo
listaNumeros=listaUsuario.split (',')
listaInvertida = listaNumeros [::-1]
#Fin
print(f'Aquí tienes la lista invertida: {listaInvertida}')

