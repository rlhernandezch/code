
class reloj:
    def __init__(self, hora,minuto,segundo,tipo):
        self.Hora = hora
        self.Minuto = minuto
        self.Segundo = segundo
        self.tipo = tipo

    def getHora(self):
        return self.Hora
    
    def getMinuto(self):
        return self.Minuto
    
    def getSegundo(self):
        return self.Segundo
    
    def getHoraCompleta(self):
        return (str(self.getHora()) +":"+str(self.getMinuto())+":"+str(self.getSegundo()) )
    
    def getTipo(self):
        return(self.tipo)
    
    def getPrecio(self,val):
        return(self.tipo[val])

