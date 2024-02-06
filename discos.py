import sqlite3

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
        conexion = sqlite3.connect("discos.db")
        cursor = conexion.cursor()
        peticion = "SELECT * FROM discos"
        cursor.execute(peticion)
        while True:
            fila = cursor.fetchone()
            if fila is None:
                break
            print(fila)
        conexion.commit()
        conexion.close()
    elif opcion == "2":
        print("Buscamos un registro")
    elif opcion == "3":
        print("Insertamos un registro")
        artista = input("Introduce el artista: ")
        anio = input("Introduce el año: ")
        titulo = input("Introduce el título: ")
        conexion = sqlite3.connect("discos.db")
        cursor = conexion.cursor()
        peticion = "INSERT INTO discos VALUES (NULL,'"+artista+"',"+str(anio)+",'"+titulo+"')"
        cursor.execute(peticion)
        conexion.commit()
        conexion.close()
        print("Tu registro se ha insertado correctamente")
    elif opcion == "4":
        print("Actualizamos un registro")
    elif opcion == "5":
        print("Eliminamos un registro")
    elif opcion == "6":
        print("Salimos")
    menu()

menu()
