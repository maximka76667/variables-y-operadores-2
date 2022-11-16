def getWeightLorenzt(h, a, s):
    if(s):
        k = 2.5
    else:
        k = 4
        
    return h - 100 - ((h - 150) / 4) + ((a - 20) / k)
    
def getWeightPerroult(h, a):
    return h - 100 + (9 * a / 100)

def getWeightBrocca(h):
    return h - 100

def getWeightMetropolitan(h):
    return 50 + 0.75 * (h - 150)


height = int(input("Altura: "))
age = int(input("Edad: "))
sex = bool(int(input("Sexo (0 - hombre, 1 - mujer): ")))
    
print("Lorenzt:", getWeightLorenzt(height, age, sex), "kg")
print("Perroult:",getWeightPerroult(height, age), "kg")
print("Brocca:",getWeightBrocca(height), "kg")
print("Metropolitan:",getWeightMetropolitan(height), "kg")