class Usuario():

    def __init__(self, nombre, credito):
        self.credito = credito
        self.nombre = nombre
        self.subastas = list()

    def aumentarCreditos(self, dinero):
        self.setCredito(self.getCredito() + dinero)

    def decrementarCreditos(self, dinero):
        self.setCredito(self.getCredito() - dinero)

    def getNombre(self):
        return self.nombre
    def setNombre(self,nom):
        self.nombre= nom

    def getCredito(self):
        return self.credito

    def setCredito(self, cre):
        self.credito = cre

    def getSubHastas(self):
        return self.subastas

    def setSubHastas(self, hol):
        self.subastas.append(hol)

class Puja(object):

    def __init__(self, pujador, puja):
        self.puja = puja
        self.pujador = pujador
    def getnombre(self):
        return self.pujador.getNombre()
    def getPuja(self):
        return self.puja
    def setPuja(self,puj):
        self.puja= puj
    def getPujador(self):
        return self.pujador
    def setPujador(self,pujador):
        return self.pujador

