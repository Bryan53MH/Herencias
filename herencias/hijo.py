from padre import persona
from padre import persona2
from madre import persona


class hijo3(persona):
    vivienda  = str

    def __init__(self, nombre, apellido, edad, vivienda):
        super().__init__(nombre, apellido, edad)
        self.vivienda

hijo3 = hijo3("Diego", "Yanez",29, "Centro historico")
padre3 = persona("German","Yanez" 55)

print(vars(hijo3))
print(vars(padre3))
print(hijo3.conversar(padre3))

class hijo4(persona2):
    edad     = int
    semestre  = str

    def __init__(self, nombre, apellido, edad, semestre):
        super().__init__(nombre, apellido)
        self.edad     = edad
        self.semestre = semestre

    def felicitar(self, padre):
        return f'Felicidades {self.nombre}, acabas de terminar tu {self.semestre}, semestre a tus {self.edad} años de edad ATT {padre.nombre} {padre.apellido}'

    padre4 = persona2("Ivan", "Borja")
    hijo4  = hijo4("Ivan", " Borja", 18, "Quinto")

    print(vars(padre4))
    print(vars(hijo4))
    print(hijo4.felicitar(padre4))

class hijofinal(padre, madre):
    nombre   = str
    apellidoPaterno = str
    apellidoMaterno  = str
    padre   = padre("", "", "", "") 
    madre   = madre("", "", "", "") 

    def __init__(self, nombre, apellido, apellidoPaterno, edad, apellidoMaterno, ciudad, padre, madre):
        super().__init__(nombre, edad, ciudad)
        self.apellidoMaterno  = apellidoMaterno
        self.apellidoPaterno  = apellidoPaterno
        self.padre  = padre
        self.madre  = madre

padrefinal = padre("German", " Yanez", 55, "Quito")
madrefinal = madre("Veronica", " Flores", 55, "Quito")
hijofinal = hijofinal("Diego", " Yanez", "Flores" ,29, "Quito", padre("German", " Yanez"))

print(vars(padrefinal))
print(vars(madrefinal))
print(vars(hijofinal))
