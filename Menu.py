from Usuari_Y_Puja import Usuario
from Subasta import Subasta
#Declaramos Pujadores
persona1 = Usuario("Toni", 100)
persona2 = Usuario("Pep", 150)
persona3 = Usuario("Enric", 300)


#Declaramos objetos de la subasta
Subasta1 = Subasta("MÓVIL", persona1)
Subasta2 = Subasta("Impresora 3D", persona2)



#Empieza el programa
print("...................................................................................")
print("COMIENZA LA SUBASTA DEL MÓVIL")
print("")
Subasta1.pujar(persona2, 100)
print("La Puja ha sido realizada por:" + Subasta1.getPujaMayor().getnombre() + " Ha pujado un total de : " + str(Subasta1.getPujaMayor().getPuja()) + "$")
print("")
print("La siguiente Puja ha sido realizada por:" + persona3.getNombre() + " Ha pujado un total de :  50 $")
Subasta1.pujar(persona3, 50)
print("")
Subasta1.ejecutar()
print("")
print(persona3.getNombre(),"intenta realizar puja pero...")
Subasta1.pujar(persona3, 200)
print(" ")
print("...................................................................................")
print("Presione una tecla para continuar")
input()
print("...................................................................................")
print("\nCOMIENZA LA SUBASTA DE LA IMPRESORA 3D")
print(persona3.getNombre(),"realiza una puja por el valor mínimmo ", )
Subasta2.pujaminima(persona3)
Subasta2.ejecutar()






print("...................................................................................")
print("")
print("PROPIETARIOS")
pujadores = list()
pujadores.append(persona1)
pujadores.append(persona2)
pujadores.append(persona3)
#Recorriendo propietarios de productos
for rec in pujadores:
    for Subasta1 in rec.getSubHastas():
        print(rec.getNombre() + " " + Subasta1.getArticulo())
print ("Y Enric no tiene ningun producto")
print("...................................................................................")
print("")


#Primer Pujador Dinero y nombre
print("PUJADORES")
print("EL primer pujador se llama: " + persona1.getNombre())
print("EL primer pujador acabo con este dinero: " + str(persona1.getCredito()))
print("")
#Segundo Pujador Dinero y nombre
print("EL segundo pujador se llama: " + persona2.getNombre())
print("EL segundo pujador acabo con este dinero: " + str(persona2.getCredito()))
print("")
#Tercer Pujador Dinero y nombre
print("EL tercer pujador se llama: " + persona3.getNombre())
print("EL tercer pujador acabo con este dinero: " + str(persona3.getCredito()))
print("...................................................................................")

