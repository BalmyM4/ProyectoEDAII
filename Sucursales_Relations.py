import Decoracion
import Sucursales_Init
import math

# ======================== Variables Distnacia ========================
class relaciones():
    distancias = []

    def __init__(self, idx, idy, sucursalx, sucursaly):
        self.idx = int(idx)
        self.idy = int(idy)
        self.sucursalx = sucursalx
        self.sucursaly = sucursaly
    
    def __str__(self):
        datos = str(self.idx)  + ", " + str(self.idy)

listaRelaciones = []
listaSucursales = Sucursales_Init.getLisaSucursales()

# ========================== Crear Relaciones ===========================
def crearRelaciones():
    global listaRelaciones
    global listaSucursales

    for i in listaSucursales:
        relaciones.distancias.append([])

    i = 0
    j = 0
    lenList = len( listaSucursales )

    while ( i < lenList ):
        j = i
        while ( j < lenList ):
            print

def calcularSucursal( sucursal ):
    global listaSucursales

    distancia = []
    i = 0
    lenList = len( listaSucursales )

    while ( i < lenList ):
        if ( sucursal.cordx != listaSucursales[i].cordx and sucursal.cordy != listaSucursales[i].cordy ):
            distancia.append( calcularDistancia( sucursal.cordx, sucursal.cordy, listaSucursales[i].cordx, listaSucursales[i].cordy ) )
        i += 1

    return distancia


def calcularDistancia( x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

# =========================== Add Relaciones ============================
def addRelaciones( sucursal ):
    global listaRelaciones

    file = open("Relaciones.csv", "w")

    for arista in listaRelaciones:
        datos =  str(arista.idx) + "," + str(arista.idx) + "\n"
        file.write( datos )

    file.close()