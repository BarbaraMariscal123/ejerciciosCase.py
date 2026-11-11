nombre = ""
apellido = ""
telefono = 0
edad = 0
correo = ""
contrasena = ""
opcion = 0


print("Bienvenido al sistema de registro de clientes")
print("---------MENU PRINCIPAL---------")
print("1. Registrar cliente")
print("2. Ver información del cliente")
print("3. Borrar información del cliente")
print("4. Modificar información del cliente")
print("5. Salir")
print("---------------------------------")
opcion = int(input("Selecciona una opción: "))

match opcion:#Aquí inicia el match, que es una validación de caso

     case 1:
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        telefono = int(input("Ingresa tu número de teléfono: "))
        edad = int(input("Ingresa tu edad: "))
        correo = input("Ingresa tu correo electrónico: ")
        contrasena = input("Ingresa tu contraseña: ")
     case 2:
        print("Nombre:", nombre, "Apellido:", apellido, "Teléfono:", telefono, "Edad:", edad, "Correo:", correo, "Contraseña:", contrasena)
     case 3:
        nombre = ""
        apellido = ""
        telefono = 0    
        edad = 0
        correo = ""
        contrasena = ""
     case 4:
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        telefono = int(input("Ingresa tu número de teléfono: "))
        edad = int(input("Ingresa tu edad: "))
        correo = input("Ingresa tu correo electrónico: ")
        contrasena = input("Ingresa tu contraseña: ")
     case 5:
        print("¡Hasta luego!")
     case _:
        print("Opción no válida")