#imprime los datos de la autora 
print("Jimenez Gamboa Issis Alexa ")
print("no.1189")
print("3W")
#imprime linea en banco para qu se vea mas limpio
print("")
#imprime el titulo del prgrama 
print("Ejercicio no.1 ")
class Estudiante():
    def __init__(self , nombre , nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print(f"Nombre:{self.nombre} \nNota: {self.nota}")

    def resultados(self):
        if self.nota >= 7:
            print("Has APROBADO!")
        else:
            print("Has REPROBADO!")

estudiante1=Estudiante("Pedro" , 5)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2=Estudiante("Elizabeth" , 7)
estudiante2.imprimir()
estudiante2.resultados()