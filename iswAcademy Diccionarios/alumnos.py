from cursos import BuscarCurso

def GestionarAlumnos():
    print("\n========== 2. Gestionar Alumnos ==========\n")
    nombre_curso = input("Ingrese el nombre del curso para gestionar alumnos: ")

    curso = BuscarCurso(nombre_curso)

    if curso is None:
        print(f"¡Error! No se ha encontrado el curso '{nombre_curso}'.")
        return

    print(f"\n===== Gestionando alumnos de: {nombre_curso} =====")
    print("a) Agregar alumnos")
    print("b) Eliminar alumnos")
    print("c) Mostrar listado de alumnos")

    opcion = input("Elija una opción (a/b/c): ").lower().strip()

    if opcion == 'a':
        nombre_alumno = input("Nombre del nuevo alumno: ").strip()
        if nombre_alumno:
            curso["alumnos"].append(nombre_alumno)
            print(f"Alumno '{nombre_alumno}' inscrito en {nombre_curso}.")
        else:
            print("El nombre del alumno no puede estar vacío.")

    elif opcion == 'b':
        nombre_alumno = input("Nombre del alumno a dar de baja: ").strip()
        if nombre_alumno in curso["alumnos"]:
            curso["alumnos"].remove(nombre_alumno)
            print(f"Alumno '{nombre_alumno}' dado de baja de {nombre_curso}.")
        else:
            print(f"Error: el alumno '{nombre_alumno}' no está inscrito en este curso.")

    elif opcion == 'c':
        print(f"\n----- Listado de alumnos en {nombre_curso} -----")
        if not curso["alumnos"]:
            print("No hay alumnos inscritos en este curso.")
        else:
            for i, alumno in enumerate(curso["alumnos"], start=1):
                print(f"{i}. {alumno}")
    else:
        print("Por favor ingrese una opción válida.")
