
class persona:
    nombre   = str
    apellido = str
    edad     = int

    def__init__(self, nombre, apellido, edad):
        self.nombre       = nombre
        self.apellido     = apellido
        self.edad         = edad

    def conversar(self, otra_persona):
        return f'hola{otra_persona.nombre}, me llamo {self.nombre},{self.apellido}, tengo {self.edad},años'


class hijo(persona):
    ciudad   = str

    def__init__(self, nombre, apellido, edad, ciudad):
        persona__init__(self, nombre, apellido, edad)
        self.ciudad = ciudad

padre = persona("Victor", "Grados", 50)
print(vars(persona))

hijo = hijo("Elena", "Grados", 25, "Quito")
print(vars(hijo))

print(padre.conversar(hijo))
print(hijo.conversar(padre))

#AGREGAR METODOS EN LA HERENCIA

class persona2:
    nombre   = str
    apellido = str

    def__init__(self, nombre, apellido, edad):
        self.nombre       = nombre
        self.apellido     = apellido

    def conversar(self, otra_persona):
        return f'hola{otra_persona.nombre}, me llamo {self.nombre},{self.apellido}, tengo {self.edad},años'

class hijo2(persona2):
    estudios       = str
    lugarEstudios  = str

    def__init__(self, nombre, apellido, materia, lugarEstudios):
        super().__init__(nombre, apellido)
        self.materia        = materia
        self.lugarEstudios  = lugarEstudios

    def informar(self, otra_persona):
        return f'Buenas tardes, {otra_persona.nombre} acabo de estudiar {self.materia} llegue hace unos 20 minutos de {self.lugarEstudios}'

padre2 = persona2("Juan","Flores")
hijo2  = hijo2("Jose","Perez", "Programacion OO", "IST YAVIRAC")

print(padre2.conversar(hijo2))

class padre:
    nombre  = str
    apellido = str
    edad = int
    ciudad  = str

    def__init__(self, nombre, apellido, edad, ciudad):
        self.nombre   = nombre
        self.apellido   = apellido
        self.edad   = edad
        self.ciudad   = ciudad

    def bienvenida(self, hijo):
        return f'BuenaS NOCHES {hijo.nombre} bienvenida a la casa, la cena esta en el micro yo me encuetro de viaje en {self.ciudad} att - {self.nombre} {self.apellido}'
        
