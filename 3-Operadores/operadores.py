# OPERADOR ARITMETICO

# 1-Define tres variables llamadas a, b y c con los valores 50, 5.0, 100.
a = 50
b = 5.0
c = 100
# 2-Define la variable d siendo la suma de a y b.
d = a + b
# 3-Define la variable e siendo la resta a y b.
e = a - b
# 4-Define la variable f con el resultado de la multiplicación d y e.
f = d * e
# 5-Define la variable g con el resultado de la división f y a.
q = f / a
# 6-Define la variable h con el módulo de f y a.
h = f % a

# OPERADOR DE COMPARACION

# 1-Define las variables a y b con los valores 50 y 10
a = 50
b = 10
# 2-Comprueba si a y b son iguales.
if a == b:
    print("Iguales")
else:
    print("Distintos")
# 3-Comprueba si a y b son distintos.
if a != b:
    print("Distintos")
else:
    print("Iguales")
# 4-Comprueba si a es mayor que b.
if a > b:
    print("A mayor")
else:
    print("B mayor")
# 5-Comprueba si a es menor o igual que b.
if a <= b:
    print("A menor o igual")
else:
    print("B mayor")

# OPERADOR DE ASIGNACION

# 1-Define una variable y asígnale el valor 999.
variable = 999
# 2-Suma 1 a la variable anterior.
variable = variable + 1
# 3-Resta 10 a la variable anterior.
variable = variable - 10
# 4-Multiplica por 10.
variable = variable * 10
# 5-Divide entre 5.
variable = variable / 5
# 6-Asigna a la variable inicial el resultado del módulo de 60
variable = variable + (60 % 60)

# OPERADORES LOGICOS

# 1-Crea las variables a, b, c y d con los valores 10, 100, 200 y 300 respectivamente.
a = 10
b = 100
c = 200
d = 300
# 2-Comprueba si a es mayor que b y c es menor que d.
if (a > b & c < d):
    print("A>B y C<D")
else:
    print("Nada")
# 3-Comprueba si la suma de a y b es mayor o igual que c o la suma de b y c es mayor o igual que d.
if (a + b >= c | b + c >= d):
    print("A+B >= C o B+C >= D")
else:
    print("Nada")

# OPERADORES DE PERTENENCIA
list1 = [1, 2, 3, 4, 5]
list2 = ['Hello', 'Word', 'Python']
list3 = ['Operator', 'Membership', 100, 200]

# 1-Comprueba si 5 está en list1.
if (5 in list1):
    print("5 está")
else:
    print("5 no está")

# 2-Comprueba si “Hello” y “Python” están en list2.
if ("Hello" in list2 and "Python" in list2):  # HAY QUE PONER "and", NO FUNCIONA CON &
    print("Hello y Python están")
else:
    print("Hello y/o Python no están")
# 3-Comprueba si list2 es igual que list3.
if (list2 == list3):  # HAY QUE PONER "and", NO FUNCIONA CON &
    print("Igules")
else:
    print("Desiguales")

# OPERADORES BIT A BIT
a = 1
b = 2

# 1-Operador AND
operador1 = a & b
# 2-Operador XOR
operador2 = a ^ b
# 3-Operador left shit
operador3 = a << 1


# OPERADORES DE IDENTIDAD
a = 3
b = 3.0

# 1-Comprueba si a es un int.
if isinstance(a, int):
    print("Es Int")
else:
    print("No es Int")

# 2-Comprueba si b es un boolean.
if isinstance(b, bool):
    print("Es Bool")
else:
    print("No es Bool")

# 3-Comprueba si b es un float.
if isinstance(b, float):
    print("Es Float")
else:
    print("No es Float")