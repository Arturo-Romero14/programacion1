
def AgregarAlum():
    alumno = input("Dime el nombre del alumno: ")
    return alumno

def EliminarAlum(curso, idAlumno):
    alumnos = curso[-1]
    if 0 <= idAlumno < len(alumnos):
        alumnos.pop(idAlumno)
    else:
        print("ID inválido.")
    return curso


def MostrarAlumn(curso):
    alumnos = curso[-1]
    print(f"=====[{curso[0]}]=====")
    if len(alumnos) == 0:
        print("No hay alumnos registrados.")
    else:
        for i in range(len(alumnos)):
            print(f"{i} - {alumnos[i]}")


def MostrarCursos(cursos):
    print("======[LISTA DE CURSOS]======")
    for i in range(len(cursos)):
        print(f"{i} - {cursos[i][0]} (Profesor: {cursos[i][1]})")



cursos = []
while True:
    curso = ["Programación I", "Jorge Norzagaray", 423,[]]
    cursos.append(curso)
    alumnos = []
    while True:
        op2 = int(input("""
            1.- Agregar Alumno
            2.- Dar de Baja Alumno
            3.- Mostrar Lista de Alumnos
            4.- Salir
                    """))
        match op2:
            case 1:
                alumno = AgregarAlum()
                alumnos.append(alumno)
                print("Se ha agregado el alumno correctamente")
            case 2: 
                MostrarAlumn(cursos[0])
                idAlum = int(input("Digite el id del alumno a dar de baja "))
                cursoEditado = EliminarAlum(cursos[0], idAlum)
                cursos[0] = cursoEditado
                print("Se ha dado de baja al alumno")
            case 3:
                MostrarCursos(cursos)
                idCurso = int(input("Digite el id del Curso"))
                MostrarAlumn(cursos[idCurso])
            case 4: 
                break
            case _:
                print("Opción Inválida")    