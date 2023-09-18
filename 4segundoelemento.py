#Programa
print ('PROGRAMA: Encontrar el segundo elemento más grande de una lista.')
#Variables
listaUsuario=(input('Ingrese una lista de números separados por comas:'))
#Algoritmo
listaNumeros=listaUsuario.split (',')
maximo= max(listaNumeros)
listaNumeros2= listaNumeros.remove(maximo)
segundoElemento = max(listaNumeros)
#Fin 
print(f'El segundo elemento más grande de la lista {listaNumeros} es: {segundoElemento}')
