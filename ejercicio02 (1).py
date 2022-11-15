#Deriman Alonso López
viajeros = {}
paises = {}
menu = '''
1) Agregar pasajeros a la lista de viajeros (puede agregar más de un
pasajero, se le preguntará al usuario si desea seguir metiendo datos de
viajeros).
2) Agregar ciudades la lista de ciudades (puede agregarse más de una
ciudad, se le preguntará al usuario si desea seguir metiendo datos de
ciudades).
3) Dado el dni de un pasajero, ver a que ciudad a viajado.
4) Dada una ciudad mostrar la cantidad de pasajeros (número) que van a
esa ciudad.
5) Dado el dni de una persona, ver a que países viaja.
6) Dado un país decir cuantos pasajeros viajan a el y mostrar el nombre
todos ellos.
7) Salir del programa.'''
while True:
    print(menu)
    opcion = input("Introduzca su opcion: ")
    if opcion.isdigit():
        match int(opcion):
            case 1:
                seguir = True
                while seguir:
                    dni = input("Introduzca el dni del viajero: ")
                    nombre = input("Introduzca el nombre del viajero: ")
                    destino = input("Introduzca la ciudad de destino: ")
                    destino = destino.lower()
                    for clave in paises:
                        for valor in paises[clave]:
                            if destino == valor:
                                if dni in viajeros:
                                    print("Lo sentimos el viajero ya esta dado de alta...")
                                if dni not in viajeros:
                                    viajeros[dni]=[nombre,[destino]]
                                    print("Viajero añadido...")
                                    print(viajeros[dni])
                    continuar = input("Desea seguir introduciendo viajeros?(s/n): ")
                    if continuar == 'n':
                        seguir = False
            case 2:
                seguir = True
                while seguir:
                    pais = input("Introduzca el pais al que desea añadir una ciudad: ")
                    ciudad = input("Nombre de la ciudad a añadir: ")
                    pais = pais.lower()
                    ciudad = ciudad.lower()
                    for clave in paises:
                        if pais == clave:
                            for ciudades in paises[clave]:
                                if ciudad in paises[clave]:
                                    print("la ciudad ya ha sido introducida.")
                                    break
                                if ciudad not in paises[clave]:
                                    paises[clave].append(ciudad)
                                    print("ciudad añadida...")
                                    print(paises[clave])
                                    break
                    if len(paises)==0:
                        paises[pais]=[ciudad]
                        print("ciudad añadida...")
                        print(paises[pais])
                        if pais not in paises:
                            paises[pais]=[ciudad]
                            print("Pais añadido")
                            print(paises)
                            break    
                    continuar = input("Desea seguir introduciendo ciudades?(s/n): ")
                    if continuar == 'n':
                        seguir = False
            case 3:
                dni = input("Introduzca el dni del viajero: ")
                if dni in viajeros:
                    for lista2 in viajeros[dni][1]:
                        print(lista2)
            case 4:
                recorrer = len(viajeros)-1
                ciudad = input("Introduzca la ciudad: ")
                contador = 0
                for dni in viajeros:
                    viajeroslista2 = viajeros[dni]
                    for i in viajeros[dni][1]:
                        if i == ciudad:
                            contador+=1
                if contador == 0:
                    print(f"No hay viajeros que visiten la ciudad {ciudad}.")
                if contador == 1 :
                    print(f"A la ciudad {ciudad} va {contador} viajero.")
                if contador >1:
                    print(f"A la ciudad {ciudad} van {contador} viajeros.")

            case 5:
                dni = input("introduzca el dni del viajero: ")
                paises_viajados = []
                print(viajeros ,"viajeros")
                for i in viajeros:
                    for j in viajeros[dni][1]:
                        ciudad_viajada = j
                        for buscador_pais in paises:
                            for ciudad in paises[buscador_pais]:
                                if ciudad_viajada==ciudad:
                                    if buscador_pais not in paises_viajados:
                                        paises_viajados+=[buscador_pais]
                print(f"El viajero ha viajado a: {paises_viajados}")
            case 7:
                print("Saliendo del programa...")
                break
#furula 🤙
                    
