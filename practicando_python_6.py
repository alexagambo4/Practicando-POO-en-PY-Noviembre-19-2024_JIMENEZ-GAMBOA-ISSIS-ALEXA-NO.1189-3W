#imprime los datos de la autora 
print("Jimenez Gamboa Issis Alexa ")
print("no.1189")
print("3W")
#imprime linea en banco para qu se vea mas limpio
print("")
#imprime el titulo del prgrama 
print("Ejercicio no.6 ")
class Marino():
    def hablar(self):
        print("Hola soy un animal marino!")

class Pulpo(Marino):
    def hablar(self):
        print("Hola soy un pulpo!")

class Foca(Marino):
    def hablar(self,mensaje):
        self.mensaje=mensaje
        print(mensaje)

marino=Marino()
marino.hablar()

pulpo=Pulpo()
pulpo.hablar()

foca=Foca()
foca.hablar("Hola soy una foca!")