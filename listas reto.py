#agregar, eliminar o modificar curso

#se desesea saber el nombre de curso, aula y lista de alumnos

#Desea saber cuantos alumnos estan inscritos de la lista

#Debera ser capaz de cambiar de instructor, aula y dar de alta y baja a alumnos

#Debe mostrar el listado de alumnos de curso

#Interfaz atractiva y solo finalizar cuando ingresen salir
def Lista_Alum():
    Alumnos = []
    while True:
        Alumnos.append(input("Ingrese el nombre de los alumnos, uno por uno. "))

def curso():

    Nombre = input("Ingrese su nombre: ")
    Instructor = input("Escriba el nombre del instructor")
    Aula = input("En que Aula sera la clase")
    Lista_Alum()

Curso = [curso]

Cursos = [Curso]
