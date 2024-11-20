#imprime los datos de la autora 
print("Jimenez Gamboa Issis Alexa ")
print("no.1189")
print("3W")
#imprime linea en banco para qu se vea mas limpio
print("")
#imprime el titulo del prgrama 
print("Ejercicio no.5 ")
class Fabrica():
    def __init__(self, llantas, color, precio):
        self._llantas=llantas
        self._color=color
        self._precio=precio

class Moto(Fabrica):
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas,self._color,self._precio))

class Carro(Fabrica):
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas,self._color,self._precio))

        print("OBJETO=moto")

moto=Moto(2, "Gris", "$200")
moto.cantidad()

print("OBJETO=carro")

carro=Carro(4 ,"Negro", "$600")
carro.cantidad()