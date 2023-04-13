# EJERCICIOS STRING

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