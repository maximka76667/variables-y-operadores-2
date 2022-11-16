import re
from math import sqrt

a = b = c = 0

def numParte(n):
    return int(n[0:n.index("x")] or 1)

s = input("f(x) = ")

# Dividimos cadena por + o - en 3 partes
result = re.split('\s*[+-]\s*', s)

# Comprobamos que valor contiene parte y cojemos el valor
for n in result:
    if re.search('x\^2$', n):
        a = numParte(n)
        
    elif re.search('x$', n):
        b = numParte(n)
        
    else:
        c = int(n)
    
print("a =", a)
print("b =", b)
print("c =", c)


try:
    # Discriminante (si nos da error no hay soluciones)
    d = sqrt(pow(b, 2) - 4 * a * c)
    
    # Calculamos soluciones x1 y x2
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)

    print("x1 =", x1)
    print("x2 =", x2)
except ValueError:
    print("No tiene soluciones")