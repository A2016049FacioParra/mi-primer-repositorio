class Estetica:
    
    def __init__(self):
        self.nombre=input('Ingresa el nombre de la Estilista: ')
        self.sueldo=float(input('Ingrese su sueldo: '))

    def imprimir(self):
        print('Nombre: ', self.nombre)
        print('Saldo: ', self.sueldo)

    def Impuestos(self):
        if self.sueldo>3000:
            print('Debe pagar impuestos.')
        else:
            print('No paga Impuestos por pobre.')


#Bloque Principal

empleado1=Estetica()
empleado1.imprimir()
empleado1.Impuestos()