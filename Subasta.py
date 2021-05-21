from Usuari_Y_Puja import Puja
from Usuari_Y_Puja import Usuario


class Subasta():
    articulo = ""
    pujaMayor = Puja("", 0)
    subastador = Usuario("", 0)
    listaDePujas = list()
    estadoSubasta = True

    def __init__(self, p, pr):
        self.producto = p
        self.subastador = pr
        pr.setSubHastas(self)

    def getArticulo(self):
        return self.producto
    def setArticulo(self, art):
        self.articulo = art

    def getsubastador(self):
        return self.subastador
    def setSubastador(self, sub):
        self.subastador = sub

    def getEstado(self):
        return self.estadoSubasta
    def setEstado(self, est):
        self.estadoSubasta = est

    def getListaDePujas(self):
        return self.listaDePujas
    def setlistaDePujas(self, lispuj):
        self.listaDePujas.append(lispuj)

    def getPujaMayor(self):
        return self.pujaMayor
    def setPujaMayor(self, pm):
        self.pujaMayor = pm

    def aceptaciónPuja(self, pujador, cantidad):
        if self.estadoSubasta:
            if not self.mismaPersona(pujador):
                if not self.dineroinnsuficiente(pujador, cantidad):
                    if self.pujaInsuficiente(cantidad):
                        print("Puja realizada Correctamente!!!!!!")
                        return True
                    else:
                        print("Puja no realizada, ya que el dinero es insuficiente")
                        return False
                else:
                    print("Dinero Insuficiente, intentelo mas tarde")
                    return False
            else:
                print("el subastador es la misma persona, no puedes hacer esto")
                return False
        else:
            print("No se puede realizar la puja, porque ya finalizó")
            return False

    def pujar(self, pujador, cantidad):
        if self.aceptaciónPuja(pujador, cantidad):
            puja = Puja(pujador, cantidad)
            self.setlistaDePujas(puja)
            self.setPujaMayor(puja)

    def pujaminima(self, pujador):
        cantidad = self.getPujaMayor().getPuja() + 1
        if self.aceptaciónPuja(pujador, cantidad):
            puja = Puja(pujador, cantidad)
            self.setlistaDePujas(puja)
            self.setPujaMayor(puja)

    def dineroinnsuficiente(self, pujador, cantidad):
        if cantidad > pujador.getCredito():
            return True
        else:
            return False

    def pujaInsuficiente(self, cantidad):
        ins = self.getPujaMayor().getPuja()
        if cantidad > ins:
            return True
        else:
            return False

    def mismaPersona(self, usuari):
        if usuari.getNombre() == self.getsubastador().getNombre():
            print("el subastador es la misma persona, no puedes hacer esto")
            return True
        else:
            return False

    def ejecutar(self):
        if self.getEstado():
            self.setEstado(False)
            self.getPujaMayor().getPujador().decrementarCreditos(self.getPujaMayor().getPuja())
            self.getsubastador().aumentarCreditos(self.getPujaMayor().getPuja())
            print("Subasta cerrada")
            return True
        else:
            print("La subasta esta crrada...")
            return False

