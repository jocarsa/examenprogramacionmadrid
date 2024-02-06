def menu():
    print("Escoge una opción:")
    print("1.-Listar registros")
    print("2.-Buscar registros")
    print("3.-Insertar registros")
    print("4.-Actualizar registros")
    print("5.-Eliminar registros")
    print("6.-Salir")
    opcion = input("Escoge una opción: ")
    if opcion == "1":
        print("Listado de registros")
    elif opcion == "2":
        print("Buscamos un registro")
    elif opcion == "3":
        print("Insertamos un registro")
    elif opcion == "4":
        print("Actualizamos un registro")
    elif opcion == "5":
        print("Eliminamos un registro")
    elif opcion == "6":
        print("Salimos")
    menu()

menu()
