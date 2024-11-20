#imprime los datos de la autora 
print("Jimenez Gamboa Issis Alexa ")
print("no.1189")
print("3W")
#imprime linea en banco para qu se vea mas limpio
print("")
#imprime el titulo del prgrama 
print("Ejercicio no.2")
p=Persona("Nombre", "edad")
p.cumpleaños()
print(f"{p.nombre} cumple {p.edad} años")

class Persona:
    def __init__(self, n, e):
        self.nombre=n
        self.edad=e

def cumpleaños(self):
    self.edad += 1

p=Persona(input("Ingrese nombre:"),int(input("Ingrese edad: ")))
p.cumpleaños()
p.cumpleaños()
print(f"{p.nombre} cumple {p.edad} años")