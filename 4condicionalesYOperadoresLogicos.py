#if y else
edad =19
if edad >= 18:
    print ("sos mayor de edad")
else:
    print ("no sos mayor de edad")


# else-if
ingreso = 1000
if ingreso == 1000:
    print("tenes 1000")
elif ingreso < 1000:
    print("tenes menos de 1000")
else:
    print("tenes mas de 1000")



#AND
resultado1 = True & True  #Devolver true
resultado2 = True & False  #Devolver false
resultado3 = False & True  #Devolver false
resultado4 = False & False  #Devolver false
#OR
resultado5 = True | True  #Devolver true
resultado6 = True | False  #Devolver true
resultado7 = False | False  #Devolver false
#NOT
resultado8 = not True  #Devolver false
resultado9 = not False  #Devolver true

print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)
print(resultado7)
print(resultado8)
print(resultado9)

