nombre = []
apellido = []
telefono = []
edad = []
correo = []
contrasena = []
opcion = []

while True:
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
        nombre.append(input("Ingresa tu nombre: "))
        apellido.append(input("Ingresa tu apellido: "))
        telefono.append(int(input("Ingresa tu número de teléfono: ")))
        edad.append(int(input("Ingresa tu edad: ")))
        correo.append(input("Ingresa tu correo electrónico: "))
        contrasena.append(input("Ingresa tu contraseña: "))
        print("Cliente registrado exitosamente, con el ID: " + str(len(nombre) - 1))
#comentario
        case 2:
            print("Lista de clientes registrados:")
            for i in range(len(name)):
                print("Id:-", i, " Con el nombre: ", nombre[i], " con el apellido: ", apellido[i], " con el teléfono: ", telefono[i], " con el correo: ", correo[i], " con la contraseña: ", contraseña[i] la edad: ", edad[i], " 
                #i += 1
        case 3:
            index = int(input("Ingresa el índice del cliente a borrar (empezando desde 0): "))
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
