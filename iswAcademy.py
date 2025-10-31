listadoCursos = []

def BuscarCurso(NombreCurso):
    for curso in listadoCursos:
        if curso["nombre"].lower() == NombreCurso.lower():
            return curso
    return None


def AgregarCurso():
    print("\n==========1. Agregar un nuevo curso==========\n")
    nombre = input("Nombre del nuevo curso: ")
    instructor = input("Nombre del instructor: ")
    aula = input("Aula asignada: ")
    alumnos = []
    curso = [nombre, instructor, aula, alumnos]
    print("¡Nuevo curso guardado!")
    return curso


def ModificarCurso():
    print("\n==========2. Modificar Curso=========\n")
    nombre = input("Ingrese el nombre del curso que desea modificar: ")
    curso = BuscarCurso(nombre)
    if BuscarCurso(nombre) == curso:
        listadoCursos
    while True:
        print(f"\n---Modificar Curso {nombre}---\n")
        print("¿Qué deseas modificar?: ")
        print("a) Instructor del curso.")
        print("b) Aula del curso.")
        opcion = input("Elige una opción a/b: ").lower()
        
        if opcion == "a":
            nuevoIns = input("Ingrese el nombre del nuevo instructor: ")
            curso["instructor"] = nuevoIns
        elif opcion == "b":
            nuevaAula = input("Ingrese la nueva aula: ")
            curso["aula"] = nuevaAula


def EliminarCurso():
    print("\n==========3. Eliminar Curso==========\n")
    nombre = input("Ingrese el nombre del curso que desea eliminar: ")
    curso = BuscarCurso(nombre)
    if BuscarCurso(nombre) == curso:
        listadoCursos.remove(curso)


def GestionarAlumnos():
    print("\n==========4. Gestionar Alumnos==========\n")
    nombre_curso = input("Ingrese el nombre edl curso para gestionar alumnos: ")

    curso = BuscarCurso(nombre_curso)

    if curso is None:
        print(f"¡Error! No se ha encontrado el curso '{nombre_curso}'.")
        return
    
    print(f"Gestionando alumnos de: {curso['nombre']}")
    print("a) Agregar alumnos")
    print("b) Eliminar alumnos")
    print("c) Mostrar listado de alumnos")

    opcion = input("Eliga una opcion (a/b/c): " ).lower()

    if opcion == 'a':
        nombre_alumno = input("NOmbre del nuevo alumno")
        curso["alumnos"].append(nombre_alumno)
        print(f"Alumno{nombre_alumno} inscrito en {curso['nombre']}")

    elif opcion == 'b':
        nombre_alumno = input("NOmbre del alumno a dar de baja: ")
        if nombre_alumno in curso["alumnos"]:
            curso["alumnos"].remove(nombre_alumno)
            print(f"Alumno '{nombre_alumno}' dado de baja de {curso['nombre']}")
        else:
            print(f"Error el alumno '{nombre_alumno}' no está en este curso")

    elif opcion == 'c':
        print(f"\n ----- Listado de alumnos en {curso['nombre']}-----")
        if not curso["alumnos"]:
            print("No hay alumnos inscritos en este curso.")
        else:
            for alumno in curso["alumnos"]:
                print(f" - {alumno}")
    else:
        print("Por favor ingrese una opción valida.")


def MostrarInformacion():
    print("\n==========5. Mostrar información de todos lo cursos.==========\n")

    if not listadoCursos:
        print("\nTodavia no hay cursos registrados!\n")
        return
    for curso in listadoCursos:
        print("---------------------------------------------")
        print(f"curso:           {curso['curso']}.")
        print(f"Instructor:      {curso['instructor']} ")
        print(f"aula:            {curso['aula']}")

        conteo = len(curso['alumnnos'])
        print(f"inscritos: {conteo} alumnos")
        print("---------------------------------------------")


def MenuInicial():
    while True:
        print("===================================")
        print("   Gestor de Cursos ISW Academy   ")
        print("===================================")
        print("1. Agregar curso")
        print("2. Modificar curso (instructor o aula)")
        print("3. Eliminar curso")
        print("4. Gestionar alumnos (inscribir, dar baja, ver lista)")
        print("5. Mostrar información de todos los cursos")
        print("6. Salir")

        opcion = int(input("Ingrese la opción que desea llevar a cabo (1, 2, 3, 4, 5, 6): "))

        match opcion:
            case 1:
                AgregarCurso()
            case 2:
                ModificarCurso()
            case 3:
                EliminarCurso()
            case 4:
                GestionarAlumnos()
            case 5:
                MostrarInformacion()
            case 6:
                print("\nSaliendo de Gestor de Cursos ISW Academy...\n")
                break
            case _:
                print("\nIngrese una opción válida.\n")

MenuInicial()