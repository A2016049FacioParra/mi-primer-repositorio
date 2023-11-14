class Personaje:
    
    def inicializar(self, nom, edd, nac):
        self.Nombre=nom
        self.Edad=edd
        self.Nacimiento=nac

    def imprimir(self):
        print ('Nombre de el alumno: ', self.Nombre)
        print ('Edad: ',self.Edad)
        print ('Fecha de nacimiento: ',self.Nacimiento)


#bloque principal
Personaje1=Personaje()
Personaje1.inicializar ('Asuka', 18, '4/12/2001')
Personaje1.imprimir()

Personaje2=Personaje()
Personaje2.inicializar('Shinji', 18, '6/6/2001')
Personaje2.imprimir()