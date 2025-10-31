cursos = {
    "Programacion I": {
        "Instructor": {
            "nombre": "Jorge Norzagaray",
            "titulo": "Ingeniero en software",
            "edad": 36
        },
        "aula": 922,
        "alumnos": []
    }
}

def BuscarCurso(NombreCurso):
    for nombre, datos in cursos.items():
        if nombre.lower() == NombreCurso.lower():
            return datos
    return None

def AgregarCurso():
    nombre = input("Nombre del nuevo curso: ")
    instructor = input("Nombre del instructor: ")
    aula = input("Aula asignada: ")

    cursos[nombre] = {
        "Instructor": instructor,
        "aula": aula,
        "alumnos": []
    }
    print(f"¡Curso '{nombre}' agregado correctamente!")

def EliminarCurso():
    print("\n========== 3. Eliminar Curso ==========\n")
    nombre = input("Ingrese el nombre del curso que desea eliminar: ")

    if nombre in cursos:
        del cursos[nombre]
        print(f"Curso '{nombre}' eliminado correctamente.")
    else:
        print(f"No se encontró el curso '{nombre}'.")

def InterfazCursos():
    while True:
        print("\n================= CURSOS =================\n")
        print("1. Agregar curso.")
        print("2. Eliminar curso.")
        print("3. Salir")

        op = int(input("Ingrese la opción que desea llevar a cabo: "))

        match op:
            case 1:
                AgregarCurso()
            case 2:
                EliminarCurso()
            case 3:
                print("Saliendo de CURSOS...")
                break
            case _:
                print("Opción no válida.")
