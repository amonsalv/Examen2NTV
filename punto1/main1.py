opcion = 100

ciclistas = []

print("1. Agregar un ciclista")
print("2. Ver los resultados")

while(opcion != 0):

    datos = {}
    opcion = int(input('Digite una opción: '))
    if opcion == 1:
        datos['nombre'] = input('Digite el nombre: ')
        datos['edad'] = input('Digite la edad: ')
        datos['país'] = input('Digite el país: ')
        datos['equipo'] = input('Digite el equipo: ')
        datos['tiempo'] = int(input('Digite el tiempo: '))
        ciclistas.append(datos)
        print(ciclistas)

    elif opcion == 2:

        tiempo = 100
        for ciclista in ciclistas:
            if ciclista['tiempo'] < tiempo:
                tiempo = ciclista['tiempo']
        print(f"¡Felicidades! El ciclista mas rápido fue {ciclista['nombre']} con un tiempo record de: {tiempo} min")
    
    elif opcion == 0:
        break
    else: 
        print('Opcion no válida')