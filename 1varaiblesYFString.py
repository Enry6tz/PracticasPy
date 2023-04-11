#tipos de datos en py

"string"
'string'
"""string con salto de 
    linea"""

#borrar variables
bienvenida = "hola"
#aca bienvenida vale hola
del bienvenida
#bienvenida 


#contatenar con +
concatenacion = "esto es una contanetacion " + "simple"
print (concatenacion)
#f string sirve para concatenar datos aunque sean de distintos tipos
nombre = "enry"
edad =30
bienvenida = f"hola {nombre} como estas? tu edad es {edad}"
print(bienvenida)

#operadores de pertenencia
#para ver si una string esta en otra usas el (in / not in) 

print ("enry" in bienvenida) #devuelve true


print ("enry" not in bienvenida) #devuelve falso


#listas , tupla, conjuntos y diccionarios

lista =[ "sring", 20, True, 1.1]
tupla = ("sring", 20, True, 1.1)
#la diferencia es que la tupla no se pueden modificar

conjunto = {"sring", 20, True, 1.1}
#los conjuntos podes modificar las posiciones y pero no el dato, no podes modificar valores, ademas no podes acceder por indice, podes ingresar pero con un bucle

diccionario = {
    'nombre' : "enry",
    'edad' : 30,
    'apellido': "seitz"
}
#La estructura de un diccionario es  key/valor, la clave es para acceder, el valor es para usar. se puede acceder a los diccionarios pero en vez del inice usas la key 
print (diccionario['nombre'])

#esto se puede hacer
lista [1]="pai"
#esto no se puede hacer
#tupla [1]= 3

#esto no se puede hacer
#conjunto [1]= 3

print (lista)
print (tupla)
print (conjunto)