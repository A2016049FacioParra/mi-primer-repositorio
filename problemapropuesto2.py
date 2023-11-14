class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        print(f'El lado mayor del triángulo es: {max(self.lado1, self.lado2, self.lado3)}')

    def es_equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print('El triángulo es equilátero.')
        else:
            print('El triángulo no es equilátero.')

triangulo1 = Triangulo(3, 3, 3)
triangulo1.lado_mayor()
triangulo1.es_equilatero()
