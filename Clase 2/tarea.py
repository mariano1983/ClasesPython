print ("Ejercicio clase 2: Recolectar los datos de n personas. ")
cantidad = int(input("Ingrese la cantidad de personas cuyos datos desea agregar: "))
for i in range(0,cantidad):
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese una edad entre 1 y 120 años: "))
    while (edad<1) or (edad>120):
        edad = int(input("No sea un forro, ingrese una edad entre 1 y 120 años: "))
    if edad < 18:
        condicion = "Menor de edad"
    elif edad <= 65:
        condicion = "Mayor de edad"
    elif edad <= 120:
        condicion = "Jubilado"
    print ("Su nombre es",nombre,apellido,"y usted es",condicion)
