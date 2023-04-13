#EJERCICIOS SET

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