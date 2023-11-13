import Sucursales_Init
import Sucursales_Relations

MAXV = 0

# ================================== Clases ====================================
class Node:
    to = 0
    cost = 0
    nxt = None

    def __init__(self, sucursal, sucursalto):
        self.sucursal = sucursal
        self.sucursalto = sucursalto

class Grafo:
    # Aristas adyacentes:
    edges = []
    # Grado de cada nodo:
    grado = []

    num_nodes = 0
    num_edges = 0
    directed = False

# =============================== Iniciar grafo ================================
def iniciar_grafo ( grafo ):
    grafo.num_nodes = 0
    grafo.num_edges = 0

    i = 0
    while ( i <= MAXV ):
        grafo.grado.append(0)
        i += 1

    i = 0
    while ( i <= MAXV ):
        grafo.edges.append(None)
        i += 1

# ================================ Crear arista ================================
def insert_edge ( grafo, intU, intV, cost, isDirected, uSucursal, vSucursal ):
    item = Node(uSucursal, vSucursal)

    item.cost = cost
    item.to = intV
    item.nxt = grafo.edges[intU]

    grafo.edges[intU] = item
    grafo.grado[intU] += 1

    if ( isDirected == False ) and ( intV != intU ):
        insert_edge (grafo, intV, intU, cost, True, vSucursal, uSucursal )
    else:
        grafo.num_edges += 1

# ================================ Crear grafo =================================
def crear_grafo ( grafo, hasCost ):
    listaRelaciones = Sucursales_Relations.listaRelaciones

    i = 0
    j = 0
    u = v = cost = 0
    number_edges = grafo.num_edges

    while ( i < number_edges ):
        while ( j < 2 ):
            u = int( listaRelaciones[i][j].idx )
            v = int( listaRelaciones[i][j].idy )
            uSucursal = listaRelaciones[i][j].sucursalx
            vSucursal = listaRelaciones[i][j].sucursaly

            cost = float(listaRelaciones[i][j].distancia * 10)

            # insert edge on the adjacent list
            insert_edge( grafo, u, v, cost, grafo.directed, uSucursal, vSucursal )
            j += 1
        i += 1

# =============================== Imprimir grafo ===============================
def imprimir_grafo ( grafo ):
    i = 1
    item = None
    print("\nADJACENT LIST:")
    string = ""
    while i <= grafo.num_nodes:
        string += str(i) + "\t"
        item = grafo.edges[i]
        while item != None:
            string += str(item.to) + ": " + str(item.cost) +"\t"
            item = item.nxt
        string += "\n"
        i += 1
    print(string)
    print()

# ================================ Grafo nuevo =================================
def newGraf():
    global MAXV
    cost = 0
    hasCost = True

    # Número de sucursales = número de aristas
    num_nodes = len(Sucursales_Init.getListaSucursales())

    # Iniciamos los nodos o vertices del grafo:
    MAXV = num_nodes
    iniciar_grafo(obj_grafo)

    obj_grafo.num_nodes = num_nodes
    obj_grafo.directed = False

    # Preguntamos número de aristas:
    Sucursales_Relations.crearRelaciones()
    obj_grafo.num_edges = len( Sucursales_Relations.listaRelaciones )
    
    # Creamos el grafo:
    crear_grafo(obj_grafo, hasCost)

# ==================================== Menú ====================================
def mostrar_menu():
    print("1. Leer grafo")
    print("2. Agregar vertice")
    print("3. Imprimir grafo")
    print("q. Salir")

def opcion_1():
    print("Has elegido la Opción 1")

def opcion_2():
    print("Has elegido la Opción 2")

def opcion_3():
    imprimir_grafo(obj_grafo)

def opcion_4():
    print("Salir")

# ==================================== Main ====================================
def main():
    
    newGraf()

    while True:
        mostrar_menu()
        seleccion = input("Elija una opción (1-4) o 'q' para salir: ")

        if ( seleccion == '1' ):
            opcion_1()

        elif ( seleccion == '2' ):
            opcion_2()

        elif ( seleccion == '3' ):
            opcion_3()

        elif ( seleccion.lower() == 'q' ):
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida.")


obj_grafo = Grafo()
main()