#imprime los datos de la autora 
print("Jimenez Gamboa Issis Alexa ")
print("no.1189")
print("3W")
#imprime linea en banco para qu se vea mas limpio
print("")
#imprime el titulo del prgrama 
print("Ejercicio no.4 ")
class Persona():
    def __init__(self,nom,ape):
        self.nombre=nom
        self.apellido=ape

def nombre_completo(self):
    print(self.nombre +" "+self.apellido)

class Estudiante(Persona):
    def __init__(self,nom,ape,carr):
        super().__init__(nom,ape)
        self.carrera=carr

def mostrar_carrera(self):
    print(self.carrera)