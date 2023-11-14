
import Decoracion

# ======================== Variables Sucursales ========================
class Sucursal:

    def __init__(self, id, name, cordx, cordy):
        self.id = int(id)
        self.name = name
        self.cordx = float(cordx)
        self.cordy = float(cordy)
        #self.data = data

    def __str__(self):
        datos = str(self.id) + ", " + str(self.name) + ", " + str(self.cordx) + ", " + str(self.cordy)
        return datos
    

listaSucursales = []

# =========================== Leer Sucursales ===========================
def readSucursales():
    global listaSucursales

    file = open("Sucursales.csv", "r")
    
    for line in file:
        datos = line.strip().split(",")
        listaSucursales.append( Sucursal( datos[0], datos[1], datos[2], datos[3] ) )

    file.close()

# =========================== Add Sucursales ============================
def newSucursales():
    newId = 1 + listaSucursales[-1].id

    Decoracion.decoracion()
    newName = input("\tDame nombre: ")
    newCordx = float(input("\tDame cord x: "))
    newCordy = float(input("\tDame cord y: "))

    newSucursal = Sucursal( newId, newName, newCordx, newCordy )
    addSucursales( newSucursal )

    return newSucursal


def addSucursales( sucursal ):
    listaSucursales.append( sucursal )

    file = open("Sucursales.csv", "a")

    datos = "\n" + str(sucursal.id) + "," + str(sucursal.name) + "," + str(sucursal.cordx) + "," + str(sucursal.cordy)
    file.write( datos )

    file.close()

# ========================== Print Sucursales ==========================
def printSucursales():
    global listaSucursales

    for sucursal in listaSucursales:
        print(sucursal)

# ========================== Get Sucursales ==========================

def getListaSucursales():
    readSucursales()

    return listaSucursales

# =========================== Main Sucursales ===========================
def main():
    readSucursales()

    printSucursales()

    newSucursales()

    printSucursales()

    espera = input("Espera: ")


#main()