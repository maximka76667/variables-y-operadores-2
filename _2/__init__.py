import re
from math import sqrt

def getNumericPart(expressionPart):
    xIndex = expressionPart.index("x")
    
    if expressionPart[0:xIndex] == "-":
        return int(-1)
    
    return int(expressionPart[0:xIndex] or 1)

# PROGRAMM START

a = b = c = 0
# La expresion se puede poner en cualquier orden y con espacios entre numeros y signos +, -
# Se pueden poner "x" sin numeros en este caso significará 1 (ej. x^2 = 1x^2)

# Ejemplo: f(x) = 4- x^2 + 4x
s = input("f(x) = ")

# Ayuda para la siguente accion que divide expresion por "+"
s = s.replace("-", "+-")

# Dividimos cadena por + en 3 partes
result = re.split('\s*[+]\s*', s)

# Comprobamos que tipo de valor contiene parte y cojemos el valor
for expressionPart in result:
    if expressionPart == "":
        continue
    
    # Borramos extra espacios
    expressionPart = expressionPart.replace(" ", "")
    
    if re.search('x\^2$', expressionPart):
        a = getNumericPart(expressionPart)
        
    elif re.search('x$', expressionPart):
        b = getNumericPart(expressionPart)
        
    else:
        c = int(expressionPart)
    
print("a =", a)
print("b =", b)
print("c =", c)

try:
    # Discriminante (si nos da ValueError no hay soluciones)
    d = sqrt(pow(b, 2) - 4 * a * c)
    
    # Calculamos soluciones x1 y x2
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)

    print("x1 =", x1)
    print("x2 =", x2)
except ValueError:
    print("No tiene soluciones")