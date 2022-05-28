import Maria.menunuevo as m
while True:
    opcionprincipal = int(input("Que desea realizar? \n 1.Crear Rostro\n 2.Buscar Rostro por Nombre\n 3.Listar Todos los Rostros \n 4. Salir\n"))
    try:
        if opcionprincipal == 1:
            m.CrearRostro()
            continue
        elif opcionprincipal == 2:
            m.BuscarporNombre()
            continue
        elif opcionprincipal == 3:
            m.Listartodo()
        elif opcionprincipal == 4:
            break
            
    except ValueError:
        print("Digite una opcion correcta")
        continue