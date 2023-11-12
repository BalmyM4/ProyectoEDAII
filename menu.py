import Lineal

def mainMenu():

    lista_usuarios = []
    while True:
        print("\nMenú Principal:")
        print("1. Crear Usuario")
        print("2. Iniciar Sesión")
        print("3. Salir")
        choice = input("Elije una opción: ")

        if choice == '1':
            Lineal.createUser("usuarios.csv")

        elif choice == '2':
            usuario = Lineal.login()
            if usuario:
                Lineal.userMenu(usuario, Lineal.usuarios)
                
        elif choice == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    mainMenu()