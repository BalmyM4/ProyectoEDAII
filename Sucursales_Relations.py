import Decoracion
import Sucursales_Init
import math

# ======================== Variables Distnacia ========================
class Relaciones():
    distancias = []

    def __init__(self, idx, idy, sucursalx, sucursaly, distancia):
        self.idx = int(idx)
        self.idy = int(idy)
        self.sucursalx = sucursalx
        self.sucursaly = sucursaly
        self.distancia = float(distancia)
    
    def __str__(self):
        datos = str(self.idx)  + ", " + str(self.idy)

listaRelaciones = []
listaSucursales = Sucursales_Init.getListaSucursales()

# ========================= Calcular Distancia ==========================
def calcularDistancia( x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

# ========================== Crear Relaciones ===========================
def encontrar_dos_mas_pequenos( lista ):
    if len(lista) < 2:
        return None

    menor1 = lista[0]
    menor2 = lista[1]

    for element in lista:
        if element.distancia < menor1.distancia:
            menor2 = menor1
            menor1 = element

        elif element.distancia < menor2.distancia and element.distancia != menor1.distancia:
            menor2 = element

    elements_mas_pequenos = [menor1, menor2]

    return elements_mas_pequenos
               
def crearRelaciones():
    global listaRelaciones
    global listaSucursales

    aux = Relaciones(0,0,None,None,0)

    for i in listaSucursales:
        aux.distancias.append([])

    i = 0
    j = 0
    lenList = len( listaSucursales )

    while ( i < lenList ):
        j = i
        while ( j < lenList ):
            if ( listaSucursales[i].cordx != listaSucursales[j].cordx and listaSucursales[i].cordy != listaSucursales[j].cordy ):
                newDistancia = calcularDistancia( listaSucursales[i].cordx, listaSucursales[i].cordy, listaSucursales[j].cordx, listaSucursales[j].cordy )
                newRelacion = Relaciones( listaSucursales[i].id, listaSucursales[j].id, listaSucursales[i], listaSucursales[j], newDistancia  )
                aux.distancias[i].append( newRelacion )
            j += 1
        i += 1
    
    for i in Relaciones.distancias:
        l = encontrar_dos_mas_pequenos( i )
        if ( l != None):
            listaRelaciones.append( l )
    
    addRelaciones()

def newRelacion( ):
    global listaRelaciones
    global listaSucursales

    sucursal = Sucursales_Init.newSucursales()

    aux = Relaciones(0,0,None,None,0)

    aux.distancias.append([])

    j = 0
    lenList = len( listaSucursales )

    while ( j < lenList ):
        if ( sucursal.cordx != listaSucursales[j].cordx and sucursal.cordy != listaSucursales[j].cordy ):
            newDistancia = calcularDistancia( sucursal.cordx, sucursal.cordy, listaSucursales[j].cordx, listaSucursales[j].cordy )
            newRelacion = Relaciones( sucursal.id, listaSucursales[j].id, sucursal, listaSucursales[j], newDistancia  )
            aux.distancias[-1].append( newRelacion )
        j += 1

    l = encontrar_dos_mas_pequenos( aux.distancias[-1] )

    file = open("Relaciones.csv", "a")

    for arista in l:
        datos =  str(arista.idx) + "," + str(arista.idy) + "," + str(arista.distancia) + "\n"
        file.write( datos )

    file.close()

# =========================== Add Relaciones ============================
def addRelaciones( ):
    global listaRelaciones

    file = open("Relaciones.csv", "w")

    for element in listaRelaciones:
        for arista in element:
            datos =  str(arista.idx) + "," + str(arista.idy) + "," + str(arista.distancia) + "\n"
            file.write( datos )

    file.close()

# =========================== Leer Sucursales ===========================
def readRelaciones():
    newlistaRelaciones = []

    file = open("Sucursales.csv", "r")
    
    for line in file:
        datos = line.strip().split(",")
        newlistaRelaciones.append( Relaciones( datos[0], datos[1] ) )

    file.close()

    return newlistaRelaciones

# =========================== Main Relations ===========================
def main():
    #crearRelaciones()
    newRelacion( )

#main()