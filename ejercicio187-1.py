class Alumno:
    def inicializar (self, nombre, nota ):
        self.Nombre=nombre
        self.Nota=nota

    def imprimir(self):
        print ('Nombre: ', self.Nombre)
        print ('Nota: ', self.Nota)
        print ('Calificacion (Regular/Libre): ', self.Nota)

    def mostrar_estado(self):
        if self.Nota>=4:
            print('Regular')
        else:
            print('Libre')


#Bloque Principal


alumno1=Alumno()
alumno1.inicializar("diego",2)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=Alumno()
alumno2.inicializar("ana",10)
alumno2.imprimir()
alumno2.mostrar_estado()