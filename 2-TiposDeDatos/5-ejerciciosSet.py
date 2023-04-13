#EJERCICIOS SET

# 1-Define un conjunto con los valores coche, motocicleta, bicicleta.
conjunto = {"coche", "motocicleta", "bicicleta"}
# 2-Añade avión al conjunto.
conjunto.add("avion")
# 3-Elimina coche del conjunto.
conjunto.remove("coche")
# 4-Crea otro conjunto con los valores avión, coche, tractor (utiliza una forma diferente que en el punto 1).
conjuntoNuevo = set()
conjuntoNuevo.add("avion")
conjuntoNuevo.add("coche")
conjuntoNuevo.add("tractor")
# 5-Crea otro conjunto con los valores que se repitan en los conjuntos anteriores.
conjuntoRepetido = conjunto & conjuntoNuevo
# 6-Muestra un conjunto con todos los valores que pertenecen al conjunto creado en el punto 1 y punto 4
print(conjuntoRepetido)