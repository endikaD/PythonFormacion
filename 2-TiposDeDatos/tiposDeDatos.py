# 1 EJERCICIOS NUMERICOS

# 1-Define cualquier número de tipo int.
numero = 5
# 2-Define cualquier número de tipo float.
numero2 = 5.5
# 3-Define cualquier número de tipo complex.
numero3 = 5 + 5j
# 4-Muestra la parte real del número definido en el punto 3.
numeroReal = numero3.real
# 5-Muestra la parte imaginaria del número definido en el punto 3.
numeroImganiario = numero3.imag


# 2 EJERCICIOS BOOLEAN

# 1-Define una variable con valor True.
verdadero = True
# 2-Define una variable con valor False.
falso = False
# 3-Define una variable con valor True mediante un entero.
variable = bool(1)

# 3 EJERCICIOS STRING

# 1-Define una variable con un string con el valor “ Master Python”.
frase = "Master Python"
# 2-Muestra la longitud de la variable anterior.
longitud=len(frase)
# 3-Muestra el primer carácter del string.
primerCaracter = frase[0]
# 4-Muestra el penúltimo carácter del string.
penultimoCaracter = frase[-2]
# 5-Elimina los espacios iniciales del string.
sinEspacios = frase.lstrip()                        #LSTRIP() ESPACIOS A LA IZQUIERDA // STRIP() IZQUIERDA Y DERECHA
# 6-Muestra los caracteres en posiciones impares.
impares = frase[::2]
# 7-Convierte todo el string en minúscula.
minuscula = frase.lower()
# 8-Separa el string por espacios en blanco.
separado = frase.split()
# 9-Reemplaza “python” por “JAVA”.
nueva = frase.replace("Python", "Java")

# 4 EJERCICIOS LISTAS

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

# 5 EJERCICIOS SET

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

# 6 EJERCICIOS SET

# 1-Define el diccionario usando dict().
diccionario = dict(coche=10, motocicleta=20, camión=30)
# 2-Define el diccionario usando { }.
diccionario2 = {"coche": 10, "motocicleta": 20, "camión": 30}
# 3-Define el diccionario usando zip().
clave = ["coche", "motocicleta", "camión"]
valor = [10, 20, 30]
diccionario3 = dict(zip(clave, valor))
# 4-Muestra los valores del diccionario.
valores = diccionario3.values()
# 5-Muestra las claves del diccionario.
claves = diccionario3.keys()
# 6-Muestra el valor de coche.
valorCoche = diccionario3["coche"]
# 7-Añade al diccionario avión con valor 100.
diccionario3.update({"avion":100})
# 8-Muestra los elementos del diccionario.
print(diccionario3)