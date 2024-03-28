class mensaje :
    mesaje =""
    listABC = ["1","2","3","4","5","6","7","8","9"]
    listaEncriptada = ["!","#","$","%","&","/","(",")","."]
    def _init_(self,inMessage):
        self.mensaje = inMenssage

    def codificar(self, inMensaje):
         listaCaracteres = list(inMensaje)
         cantidadCaracteres = len(listaCaracteres)
         palabraCodificada = ""
         for i in range(0, cantidadCaracteres):
              caracter = listaCaracteres [i]
              for y in range (0, len(self.listaEncriptada)):
                  if(caracter == self.listaABC[y]):
                      palabraCodificada = palabraCodificada + self.listaEncriptada [y]
         return palabraCodificada
     
  
    def _init_(self,inMessage):
        self.mensaje = inMenssage

    def decodificar(self,inMensaje):
         listaCaracteres = list(inMensaje)
         cantidadCaracteres = len(listaCaracteres)
         palabraDecodificada = ""
         for i in range(0, cantidadCaracteres):
              caracter = listaCaracteres [i]
              for y in range (0, len (self.listaEncriptada)):
                  if(caracter == self.listaEncriptada[y]):
                      palabraDecodificada = palabraDecodificada + self.listaABC [y]
         return palabraDecodificada
    
