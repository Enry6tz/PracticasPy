cadena1 = "Hola BUENAS"
cadena2 =  "Todo bien? "
cadena3 = "1234"
cadena4 = "1234letra"
cadena6 = "letrass"
#el dir es una FUNCION. es como un help te dice que es lo que podes hacer con el parametro

#print (dir (cadena1))  //comentado porque es mucho texto

#UPPER convierte en mayusculas

print (cadena1.upper())

#LOWER convierte a minuscula
print (cadena2.lower()) 

#CAPITALIZE pone todo en minusculas y la primer letra en mayusculas

print (cadena1.capitalize())

#FIND encuentra la primera aparicion del valor especificado, sino encuentra devuelve 1

print (cadena1.find("Hola")) #posicion 0
print (cadena2.find("hola")) #no existe devuelve -1
print (cadena2.find("b")) #devuelve 5


#INDEX encuentra la primera aparicion del valor especificado, sino devuelve una excepcion
print (cadena1.index("Hola")) #posicion 0
#print (cadena2.index("hola")) #no existe devuelve una exepcion
print (cadena2.index("b")) #devuelve 5

#ISNUMERIC si es un NUMERICO devuelve true
print (cadena1.isnumeric())
print (cadena3.isnumeric())

#ISALPHA si es un ALFA NUMERICO devuelve true el espacio o caracteres especiales no cuentan 
print (cadena4.isalpha())
print (cadena6.isalpha())

#COUNT devuelve el numero de coincidencias de una subcadena en la cadena dada. sino hay es cero
print (cadena6.count("s")) #devuelve 2
print (cadena6.count("ss")) #devuelve 1
print (cadena6.count("2")) #devuelve 0
#LEN es FUNCION. cuenta los caracteres de una cadena
print (len(cadena2)) #devuelve 11
#ENDSWITH verifica si una cadena comienza con 
print (cadena3.endswith("4")) #devuelve true
#STARTSWITH verifica si una cadena termina con
print (cadena3.startswith("4")) #devuelve falso
#REPLACE reemplaza un valor por otro
print (cadena1.replace("Hola", "Holi")) 
print (cadena1.replace("Holaa", "Holi"))  #no encuenta coincidencia, devuelve la cadena anterior

#SPIT separa en cadena por el parametro dado
cadenaSPIT = "hola,como,estas.todo,bien?"
print (cadenaSPIT.split(","))
#esto devuelve una lista con todos los elementos separados por la "," ['hola', 'como', 'estas.todo', 'bien?']]