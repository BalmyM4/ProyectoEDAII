MAXV = 0

# ================================== Clases ====================================
class Node:
    to = 0
    cost = 0
    nxt = None

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
def insert_edge ( grafo, intU, intV, cost, isDirected ):
    item = Node()

    item.cost = cost
    item.to = intV
    item.nxt = grafo.edges[intU]

    grafo.edges[intU] = item
    grafo.grado[intU] += 1

    if ( isDirected == False ) and ( intV != intU ):
        insert_edge (grafo, intV, intU, cost, True )
    else:
        grafo.num_edges += 1

# ================================ Crear grafo =================================
def crear_grafo ( grafo, hasCost ):
    i = 0
    u = v = cost = 0
    number_edges = grafo.num_edges

    while ( i < number_edges ):
        print("\nCrea arista (u, v)")
        u = int(input('\n\tu: '))
        v = int(input('\tv: '))

        if ( hasCost == True ):
            print("\nInsertar costo o peso de la arista:")
            cost = int(input('\n\tCost / weight: '))
        else:
            cost = 1

        # insert edge on the adjacent list
        insert_edge( grafo, u, v, cost, grafo.directed )
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
    print("Has elegido la Opción 3")

def opcion_4():
    print("Has elegido la Opción 4")

# ==================================== Main ====================================
def main():
    global MAXV
    cost = 0
    hasCost = True

    # Preguntamos número de vertices o nodos:
    print("\nNúmero de vertices: ", end="")
    num_nodes = int(input())

    # Iniciamos los nodos o vertices del grafo:
    MAXV = num_nodes
    iniciar_grafo(obj_grafo)

    obj_grafo.num_nodes = num_nodes
    obj_grafo.directed = False

    # Preguntamos número de aristas:
    print("\nNúmero de aristas: ", end="")
    obj_grafo.num_edges = int(input())
    
    # Creamos el grafo:
    crear_grafo(obj_grafo, hasCost)

    # Imprimimos el grafo:
    imprimir_grafo(obj_grafo)

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