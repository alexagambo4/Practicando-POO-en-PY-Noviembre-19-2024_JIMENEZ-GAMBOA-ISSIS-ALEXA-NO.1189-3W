#imprime los datos de la autora 
print("Jimenez Gamboa Issis Alexa ")
print("no.1189")
print("3W")
#imprime linea en banco para qu se vea mas limpio
print("")
#imprime el titulo del prgrama 
print("Ejercicio no.7 ")
class Universidad():
    def __init__(self,Nombre):
        self.Nombre=Nombre

class Carerra():
    def carrera(self,especialidad):
        self.especialidad=especialidad

class Estudiante(Universidad,Carerra):
    def datos(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Universidad {self.Nombre}")

persona=Estudiante("Hardvard")
persona.carrera("Ingeniería mecatronica")
persona.datos("Mike", 19)