class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad debe ser un valor positivo")

    def set_dni(self, dni):
        if len(dni) == 9:
            self.dni = dni
        else:
            print("El DNI debe tener 9 dígitos")

    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad

    def get_dni(self):
        return self.dni

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    def es_mayor_de_edad(self):
        return self.edad >= 18 if self.edad is not None else False

# Crear una instancia de la clase Persona
persona1 = Persona()

# Establecer atributos usando setters
persona1.set_nombre("Juan Pérez")
persona1.set_edad(17)
persona1.set_dni("123456789")

# Mostrar los datos de la persona
persona1.mostrar()

# Comprobar si es mayor de edad
if persona1.es_mayor_de_edad():
    print("Es mayor de edad")
else:
    print("No es mayor de edad")
