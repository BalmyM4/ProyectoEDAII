import csv
import random
import string
################################################################
lista_usuarios = []
usuarios = []
class Usuario:
    def __init__(self, user, password, nip, numCard, indentifier):
        self.user = user
        self.password = password
        self.nip = nip
        self.numCard = numCard
        self.indentifier = indentifier
        self.fondo = 0

    def retirar_dinero(self, cantidad):
        if cantidad > 0 and cantidad <= self.fondo:
            print(f"Retiraste ${cantidad}. Tu saldo actual es de ${self.fondo}.")
            self.fondo -= cantidad
        else:
            print("Cantidad no válida o insuficientes fondos.")

    def depositar_dinero(self, cantidad):
        if cantidad > 0:
            self.fondo += cantidad
            print(f"Depositaste ${cantidad}. Tu saldo actual es de ${self.fondo}.")
        else:
            print("Cantidad de depósito no válida.")

    def transferir_dinero(self, destino, cantidad, lista_usuarios):
        if cantidad > 0 and self.fondo >= cantidad:
            self.fondo -= cantidad
            destino.fondo += cantidad
            print(f"Transferiste ${cantidad} a {destino.user}.")
            print(f"Tu saldo actual es de ${self.fondo}.")
        else:
            print("Error en la transferencia por falta de saldo.")

    def encontrar_usuario(self, receptor, lista_usuarios):
        for usuario in lista_usuarios:
            if usuario.user == receptor:
                return usuario
        return None
        

    def registro(self, accion, cantidad):
        archivo_accion = f"{self.user}_{accion}.csv"
        archivo_general = "acciones_generales.csv"

        with open(archivo_accion, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.user, accion, cantidad])

        with open(archivo_general, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.user, accion, cantidad])
####################################################################
class Administrador(Usuario):
    def __init__(self, user, password, nip, numCard, indentifier, access_level):
        super().__init__(user, password, nip, numCard, indentifier)
        self.nivel_acceso = access_level

def generateID():
    return ''.join(random.choice(string.digits) for _ in range(5))

def createUser(archivo_csv):
    user = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    nip = input("NIP: ")
    numCard = input("Número de tarjeta: ")
    typeUser = input("Tipo de usuario (Usuario/Administrador): ")
    indentifier = generateID()

    nuevo_usuario = [indentifier, user, password, nip, numCard, typeUser] 
    
    with open(archivo_csv, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(nuevo_usuario)

    print(f"Usuario '{user}' creado y guardado en el archivo CSV.")


def login():
    usuarios = [] 

    with open("usuarios.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            usuarios.append(row)

    user = input("Nombre de usuario: ")
    password = input("Contraseña: ")

    for usuario in usuarios:
        if usuario[1] == user and usuario[2] == password:
            if usuario[5].lower() == "administrador":
                print("Inicio de sesión exitoso como administrador.")
                return Administrador(user, password, usuario[3], usuario[4], usuario[0], "administrador")
            else:
                print("Inicio de sesión exitoso como usuario.")
                return Usuario(user, password, usuario[3], usuario[4], usuario[0])

    print("Credenciales incorrectas. Inicio de sesión fallido.")
    return None



def userMenu(user, lista_usuarios):
    while True:
        print("\nMenú de usuario:")
        print("1. Retirar dinero")
        print("2. Depositar dinero")
        print("3. Transferencia de dinero")
        print("4. Cerrar sesión")
        choice = input("Elije una opción: ")

        if choice == '1':
            cantidad = float(input("Ingresa la cantidad a retirar: $"))
            user.retirar_dinero(cantidad)
            user.registro("retirar", cantidad) 
        elif choice == '2':
            cantidad_str = input("Ingresa la cantidad a depositar: $")
            if cantidad_str.strip():
                cantidad = float(cantidad_str)
                user.depositar_dinero(cantidad)
                user.registro("depositar", cantidad)
            else:
                print("Por favor, ingresa una cantidad válida.")
        elif choice == '3':
            receptor_nombre = input("Ingresa el nombre de usuario del receptor: ")
    
            receptor_obj = user.encontrar_usuario(receptor_nombre, usuarios)
            if receptor_obj:
                cantidad_str = input("Ingresa la cantidad a transferir: $")
                if cantidad_str.strip():
                    cantidad = float(cantidad_str)
                    user.transferir_dinero(receptor_obj, cantidad)
                    user.registro("transferir", cantidad)
                else:
                    print("Por favor, ingresa una cantidad válida.")
            else:
                print("Usuario receptor no encontrado.")
        elif choice == '4':
            print("Cerrando sesión.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

##############################################################################





