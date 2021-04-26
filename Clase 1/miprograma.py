print("Hola mundo, vamos con el primer ejercicio!!!!")

nombre = input("Ingrese su nombre de pila: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")


edad =int(edad)

if edad < 18:
    condicion = "menor"
elif edad < 65:
    condicion = "mayor"
elif edad < 120:
    condicion = "jubilado"
else:
    condicion = "un cadaver"

print ("Su nombre es",nombre,apellido,"y usted es",condicion,)
