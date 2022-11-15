#Deriman Alonso López
ventas=[]
clientes = []
client = []
menu = '''1) Añadir cliente
(2) Eliminar cliente
(3) Añadir factura
(4) Procesar facturación del mes
(5) Listar todos los clientes
(6) Terminar. '''
seguir = True
while True:
    print()
    print(menu)
    opcion = input("Introduzca su opcion: ")
    seguir = True
    if opcion.isdigit():
        opcion = int(opcion)
        match opcion:
            case 1:
                nombre_apellidos = input("Introduzca el nombre y apellidos del cliente: ")
                cif = input("Introduzca el cif del cliente: ")
                direccion = input("Introduzca la direccion del cliente: ")
                clientes += [(nombre_apellidos,cif,direccion)]
                print("Cliente añadido...")
                print(clientes)
            case 2:
                while seguir:
                    nombre = input("Introduzca el nombre del cliente a eliminar: ")
                    if seguir == False:
                        break
                    for i in ventas:
                        for j in i:
                            if j == nombre:
                                print("No se puede eliminar porque se encuentra en la lista de ventas")
                                seguir = False
                            if seguir:
                                for h in clientes:
                                    for k in h:
                                        if k == nombre:
                                            clientes.remove(h)
                                            print("Se ha eliminado el cliente")
                                            print(clientes)
                                            seguir = False
                            else:
                                pass
            case 3:
                cliente_factura = input("Introduzca el cliente a añadir la factura: ")
                dia = input("Introduzca el dia del mes de la factura: ")
                monto = input("introduzca el monto de la factura: ")
                contador_clientes = len(clientes)+1
                for i in clientes:
                    contador_clientes -=1
                    for j in i:
                        if j == cliente_factura:
                            monto=float(monto)
                            dia = int(dia)
                            if dia <= 31 and dia >=1:
                                ventas += [(cliente_factura,dia,monto)]
                            break
                    if contador_clientes == 0:
                        print("Lo sentimos, el cliente no figura en la lista...")
                        break
            case 4:
                clientes_factura_realizada = []
                client = []
                for elementos in ventas:
                    if len(client)>0:
                        print(f"Factura empleado {client[0]}: total de dias facturados: {client[1]}, monto total facturado {client[2]}")
                    clientes_factura_realizada += client
                    client = []
                    for i in range(len(ventas)):
                        for j in range(len(ventas[i])):
                            if elementos[0]==ventas[i][j] and elementos[0] not in clientes_factura_realizada:
                                if elementos[0] in client:
                                    client[1]+=1
                                    client[2]+=ventas[i][j+2]
                                if elementos[0] not in client:
                                    client += [elementos[0],1,ventas[i][j+2]]
                if len(client)>0:
                    print(f"Factura empleado {client[0]}: total de dias facturados: {client[1]}, monto total facturado {client[2]}")
            case 5:
                print(clientes)
            case 6:
                break
#furula 🤙