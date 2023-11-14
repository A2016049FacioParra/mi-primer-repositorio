class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}\nEdad: {self.edad}')

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(f'{self.nombre} es mayor de edad.')
        else:
            print(f'{self.nombre} no es mayor de edad.')

persona1 = Persona('Juan', 20)
persona1.mostrar_datos()
persona1.es_mayor_de_edad()
