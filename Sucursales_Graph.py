import Sucursales_Init
import Sucursales_Relations
import Decoracion

# ================================== Clases ====================================
class Node:
    to = 0
    cost = 0
    nxt = None

    # BFS
    prev = None

    # color: 0-blank, 1-gray, 2-black
    color = 0
    distance = -1

    def __init__(self, sucursal, sucursalto):
        self.sucursal = sucursal
        self.sucursalto = sucursalto

class Graph:
# ================================ Init graph ================================    
    def __init__ (self, numNodes, numEdges, cost):
        self.edges = [] 
        self.grade = []
        self.numNodes = numNodes
        self.numEdges = numEdges
        self.directed = False
        self.hasCost = True if cost == 1 else False

        i = 0
        while i <= self.numNodes:
            self.grade.append(0) 
            self.edges.append(None)
            i += 1

# ================================ Crear arista ================================
    def insert_edge(self, intU, intV, intCost, isDirected, uSucursal, vSucursal):

        item = Node( uSucursal, vSucursal )
        item.cost = intCost
        item.to = intV
        item.nxt = self.edges[intU]

        self.edges [intU] = item
        self.grade [intU] += 1

        if ( isDirected == False ) and ( intV != intU ):
            self.insert_edge(intV, intU, intCost, True, vSucursal, uSucursal)

# ================================ Crear grafo =================================
    def crear_grafo (self):
        global listaRelaciones

        i = 1
        j = 0
        while i <= self.numEdges:
            j = 0
            while ( j < 2 ):
                u = int( listaRelaciones[i-1][j].idx )
                v = int( listaRelaciones[i-1][j].idy )
                uSucursal = listaRelaciones[i-1][j].sucursalx
                vSucursal = listaRelaciones[i-1][j].sucursaly

                cost = float(listaRelaciones[i-1][j].distancia * 10)

                self.insert_edge( u, v, cost, self.directed, uSucursal, vSucursal )
                j += 1
            i += 1

# =============================== Imprimir grafo ===============================
    def print(self): 
        i = 1
        item = None 
        string=""

        while ( i <= self.numNodes ): 
            string += str(i) + "\t" 
            item = self.edges[i]

            while item != None:
                string += str(item.to) + ": " + str(item.cost) + "\t"
                item = item.nxt

            string += "\n"
            i += 1

        print(string)

# =============================== BFS ===============================
    #color: blank, 1 gray, 2 - black 
    def breadth_first_search(self, intSource):                                     
        self.edges[intSource].color = 1                                            
        self.edges[intSource].distance = 0                                         
        self.edges[intSource].prev = None                                          
        queue = []                                                                 
        queue.append(intSource)                                                    
                                                                                
        while len(queue) != 0:                                                     
            u = queue.pop(0)                                                       
            v = self.edges[u]                                                      
                                                                                
            while v != None:                                                       
                if ( self.edges[v.to] != None ):                                   
                    if ( self.edges[v.to].color == 0 ):                            
                        self.edges[v.to].color = 1                                 
                        self.edges[v.to].distance = self.edges[u].distance + 1     
                        self.edges[v.to].prev = u                                  
                        queue.append(v.to)                                         
                v = v.nxt                                                          
            self.edges[u].color = 2                                                
                                                                                
                                                                                
    def print_color(self):
        i = 1
        print("BREADTH FIRST SEARCH:") 
        string = ""

        while ( i <= self.numNodes ):
            if ( self.edges [i] != None ):
                if ( self.edges[i].color == 0 ):
                    color = "blank"
                    
                elif ( self.edges[i].color == 1 ):
                    color = "gray"

                else:
                    color = "black"

                cont = 0
                tabs = ""

                while ( cont < self.edges[i].distance ):
                    tabs += "\t"
                    cont += 1

                string += tabs + str(i) + ": " + color + "-" + str(self.edges[i].distance) + "-" + str(self.edges[i].sucursal.id) + "\t" 
                string += "\n"
            i += 1
        print(string)

# ================================ Grafo nuevo =================================
def newGraf():
    global listaRelaciones
    global objGraph

    cost = 0
    hasCost = True

    # Número de sucursales = número de vertices
    num_nodes = len(Sucursales_Init.listaSucursales)

    # Número de aristas:
    Sucursales_Relations.crearRelaciones()
    listaRelaciones = Sucursales_Relations.listaRelaciones

    num_edges = len( listaRelaciones )

    source = 1

    objGraph = Graph(num_nodes, num_edges, True)
    objGraph.crear_grafo()

# ==================================== Menú ====================================
def mostrar_menu():
    Decoracion.decoracion()
    print("\t\t\tMenú de sucursales.")
    Decoracion.decoracion()
    print("\t1. Leer grafo")
    print("\t2. Agregar sucursal")
    print("\t3. Imprimir grafo")
    print("\t4. Imprimir lista sucursales")
    print("\t5. BFS")
    print("\tq. Salir")

def opcion_1():
    global listaRelaciones

    Decoracion.decoracion()
    listaRelaciones = Sucursales_Relations.readRelaciones()

def opcion_2():
    global objGraph

    Sucursales_Relations.newRelacion()
    newGraf()

def opcion_3():
    global objGraph
    Decoracion.decoracion()
    objGraph.print()

def opcion_4():
    Decoracion.decoracion()
    Sucursales_Init.printSucursales()

def opcion_5():
    global objGraph
    Decoracion.decoracion()
    objGraph.breadth_first_search(1)
    objGraph.print_color()

# ==================================== Main ====================================
def main():
    
    newGraf()

    while True:
        mostrar_menu()
        seleccion = input("\n\tOpción: ")

        if ( seleccion == '1' ):
            opcion_1()

        elif ( seleccion == '2' ):
            opcion_2()

        elif ( seleccion == '3' ):
            opcion_3()
        
        elif ( seleccion == '4' ):
            opcion_4()

        elif ( seleccion == '5' ):
            opcion_5()    

        elif ( seleccion.lower() == 'q' ):
            Decoracion.decoracion()
            print("\t\tSaliendo.")
            Decoracion.decoracion()
            break

        else:
            Decoracion.decoracion()
            print("\tError: Opción no válida.")


Sucursales_Init.getListaSucursales()
objGraph = None
        
main()