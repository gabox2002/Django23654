
#Ej7
'''
Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
titular (que es una persona) y cantidad (puede tener decimales). 
El titular será obligatorio y la cantidad es opcional. 
Crear los siguientes métodos para la clase: 
*Un constructor, donde los datos pueden estar vacíos. 
*Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero. 
*mostrar(): Muestra los datos de la cuenta. 
*ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. 
*retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad  # Atributo privado para control interno

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.cantidad = cantidad
        else:
            print("La cantidad no puede ser negativa.")

    def mostrar(self):
        print(f"Titular: {self.titular.nombre}")
        print(f"Cantidad: {self.cantidad}")

    def ingresar(self, cantidad):
        if cantidad >= 0:
            self.cantidad += cantidad
            print(f"Se ingresaron {cantidad} pesos a la cuenta.")
        else:
            print("La cantidad ingresada no puede ser negativa.")

    def retirar(self, cantidad):
        self.cantidad -= cantidad
        print(f"Se retiraron {cantidad} pesos de la cuenta.")

# Crear objetos de prueba
titular1 = Persona("Juan", 17)
cuenta1 = Cuenta(titular1, 100.0)
cuenta1.mostrar()
cuenta1.ingresar(50.0)
cuenta1.retirar(50.0)
cuenta1.mostrar()

#Ej8
'''
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuentaJoven que deriva de la clase creada en el punto 7. 
Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. 
Crear los siguientes métodos para la clase: 
*Un constructor. 
*Los setters y getters para el nuevo atributo. 
*En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario. 
*Además, la retirada de dinero sólo se podrá hacer si el titular es válido. 
*El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
'''
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    def set_bonificacion(self, bonificacion):
        if 0 <= bonificacion <= 100:
            self.bonificacion = bonificacion
        else:
            print("La bonificación debe estar entre 0 y 100.")

    def es_titular_valido(self):
        return 18 <= self.titular.edad < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
            print("Retiro exitoso.")
        else:
            print("No se puede realizar el retiro, el titular no es válido.")

    def mostrar(self):
        super().mostrar()
        print(f"Tipo: Cuenta Joven")
        print(f"Bonificación: {self.bonificacion}%")


# Crear objetos de prueba

titular_joven = Persona("Ana", 22)
cuenta_joven = CuentaJoven(titular_joven, 200.0, 5.0)
cuenta_joven.mostrar()
cuenta_joven.retirar(70.0)