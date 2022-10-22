from Persona import Banco


persona1 = Banco()

persona1.nombre = input('Digite el nombre del cliente: ')
persona1.apellido = input('Didite el apellido del cliente: ')
persona1.cedula = int(input('Digite la cedula del cliente: '))
persona1.ciudad = input('Digite la ciudad del cliente: ')
persona1.numCuenta = input('Digite el numero de cuenta: ')
persona1.saldo = int(input('Digite el saldo: '))

agregar = 0

opcion = int(input("Elija una opción: 1. Consultar cliente, 0 salir: "))
while (opcion != 0):
    print(persona1.saldo)
    consultar = int(input("Ingrese la cedula a consultar: "))
    if consultar == persona1.cedula:
        print(f"La persona es: {persona1.nombre} {persona1.apellido}")
        menu = int(input('Ingrese si desea 1 retirar o 2 ingresar: '))
        if menu == 1:
            retirar = int(input("Valor a retirar: "))
            persona1.retiro = retirar
            persona1.saldo = persona1.saldo-persona1.retiro
            print(
                f"El retiro de {persona1.nombre} fue de {retirar} el saldo restante es: {persona1.saldo}")
        elif menu == 2:
            agregar = int(input("Valor a ingresar: "))
            persona1.ingreso = agregar
            persona1.saldo = persona1.saldo + persona1.ingreso
            print(
                f"La consignación de {persona1.nombre} fue de {agregar} el saldo total es: {persona1.saldo}")
        else:
            print("Opcion no válida")
    else:
        print("Usuario no encontrado")
    opcion = int(input("Elija una opción: 1. Consultar cliente, 0 salir: "))