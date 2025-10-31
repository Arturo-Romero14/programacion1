import alumnos
import cursos


while True:
    print("\n============= BIENVENIDO A ISW ACADEMY =============\n")
    print("¿Qué acción desea llevar a cabo?")
    print("1. Cursos")
    print("2. Alumnos")
    print("3. Salir")

    try:
        op = int(input("Ingrese la opción: "))
    except ValueError:
        print("Por favor ingrese un número válido.")
        continue

    match op:
        case 1:
            cursos.InterfazCursos()
        case 2:
            alumnos.GestionarAlumnos()
        case 3:
            print("Saliendo de ISW Academy...")
            break
        case _:
            print("Por favor ingrese una respuesta válida.")
