class Incidencia:
    idIncidencia=0
    minutos=0
    segundos=0
    horas=0
    cerrada=False

    def __init__(self,idIncidencia,cerrada,minutos,segundos,horas):
        self.idIncidencia=idIncidencia
        self.cerrada=cerrada
        self.minutos=minutos
        self.segundos=segundos
        self.horas=horas

    def __init__(self,idIncidencia=None,cerrada=None,horas=None,minutos=None,segundos=None):
        self.idIncidencia=idIncidencia
        self.cerrada=cerrada
        self.minutos=minutos
        self.segundos=segundos
        self.horas=horas

    def getIdIncidencia(self):
        return self.idIncidencia

    def getMinutos(self):
        return self.minutos

    def getSegundos(self):
        return self.segundos

    def getHoras(self):
        return self.horas

    def getCerrada(self):
        return self.cerrada
