#EJERCICIOS LISTAS

# 1-Define una lista con los valores 10,20,'Hello',20.5
lista = [10,20,'Hello',20.5]
# 2-Añade “Word” al final de la lista.
lista.append('Word')
# 3-Añade “Python” al principio de la lista.
lista.insert(0,'Python')
# 4-Elimina el segundo valor de la lista.
lista.pop(1)
# 5-Crea una segunda lista con los valores 20, 40, ‘Bye’ (utiliza una forma diferente que en el punto 1)
segundaLista = []
segundaLista.append(20)
segundaLista.append(40)
segundaLista.append('Bye')
# 6-Une las dos listas.
listaSumada = lista + segundaLista
# 7-Muestra la lista final.
print(listaSumada)