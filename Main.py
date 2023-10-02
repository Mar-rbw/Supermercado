from Tecnologia import Tecnologia
from Transporte import Transporte
from Consola import Consola
from Tv import Tv
from Scooter import Scooter
from Bicicleta import Bicicleta

def registrarTv():
    print("Registrar TV:")
    voltaje = int(input("Voltaje: "))
    precio = float(input("Precio: "))
    eficiencia = input("Eficiencia (A/ B/ C/ D/ E/ F): ")
    marca = input("Marca: ")
    tamanio = float(input("Tamaño (en pulgadas): "))

    tv = Tv(voltaje, precio, eficiencia, marca, tamanio)

    listaTVs.append(tv)

    print("TV registrado con éxito.")


def registrarConsola():
    print("Registrar Consola:")
    voltaje = int(input("Voltaje: "))
    precio = float(input("Precio: "))
    eficiencia = input("Eficiencia (A/B/C/D/E/F): ")
    marca = input("Marca: ")
    nombreConsola = input("Nombre de la Consola: ")
    version = input("Versión: ")

    consola = Consola(voltaje, precio, eficiencia, marca, nombreConsola, version)

    listaConsolas.append(consola)

    print("Consola registrada con éxito.")
    
    
def registrarScooter():
    print("Registrar Scooter:")
    voltaje = int(input("Voltaje: "))
    precio = float(input("Precio: "))
    eficiencia = input("Eficiencia (A/B/C/D/E/F): ")
    marca = input("Marca: ")
    aro = float(input("Aro: "))
    velocidad = int(input("Velocidad (km/h): "))
    peso = float(input("Peso (kg): "))

    scooter = Scooter(voltaje, precio, eficiencia, marca, aro, velocidad, peso)

    listaScooters.append(scooter)

    print("Scooter registrado con éxito.")
    

def registrarBicicleta():
    print("Registrar Bicicleta:")
    aro = float(input("Aro: "))
    peso = float(input("Peso (kg): "))
    precio = float(input("Precio: "))
    marca = input("Marca: ")

    bicicleta = Bicicleta(aro, peso, precio, marca)

    listaBicicletas.append(bicicleta)

    print("Bicicleta registrada con éxito.")
    
    
""" def cotizarTvs():
    if not listaTVs:
        print("No hay TVs registrados.")
        return

    print("Cotización de TVs:")
    for index, tv in enumerate(listaTVs, start=1):
        print(f"TV {index}:")
        print(f"Marca: {tv.get_marca()}")
        print(f"Voltaje: {tv.get_voltaje()}")
        print(f"Precio: {tv.get_precio()}")
        print(f"Eficiencia: {tv.get_eficiencia()}")
        print(f"Tamaño: {tv.get_tamanio()} pulgadas")
         """
def cotizarTvs():
    if not listaTVs:
        print("No hay TVs registrados.")
        return
    
    print("Cotizando TVs:")
    for tv in listaTVs:
        caracteristicas_tv = tv.__str__()
        print(f"{caracteristicas_tv}\n")
        
def cotizarConsolas():
    if not listaConsolas:
        print("No hay Consolas registradas para cotizar.")
        return

    print("Cotizando Consolas:")
    for consola in listaConsolas:
        caracteristicas_consolas = consola.__str__()
        print(f"{caracteristicas_consolas}\n")
 

def cotizarScooters():
    if not listaScooters:
        print("No hay Scooters registrados para cotizar.")
        return

    print("Cotizando Scooters:")
    for scooter in listaScooters:
        caracteristicas_scooters = scooter.__str__()
        print(f"{caracteristicas_scooters}\n")


def cotizarBicicletas():
    if not listaBicicletas:
        print("No hay Bicicletas registradas para cotizar.")
        return

    print("Cotizando Bicicleta:")
    for bicicleta in listaBicicletas:
        caracteristicas_bicicleta = bicicleta.__str__()
        print(f"{caracteristicas_bicicleta}\n")


def menu():
    while True:
        print("-" * 30)
        print("Bienvenido al menu")
        print("1. Registrar TV")
        print("2. Registrar Consola")
        print("3. Registrar Scooter")
        print("4. Registrar Bicicleta")
        print("5. Cotizar TVs")
        print("6. Cotizar Consolas")
        print("7. Cotizar Scooters")
        print("8. Cotizar Bicicletas")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")
        print("-" * 30)
        
        
        if opcion == "1":
            registrarTv()
        elif opcion == "2":
            registrarConsola()
        elif opcion == "3":
            registrarScooter()
        elif opcion == "4":
            registrarBicicleta()
        elif opcion == "5":
            cotizarTvs()
        elif opcion == "6":
            cotizarConsolas()
        elif opcion == "7":
            cotizarScooters()
        elif opcion == "8":
            cotizarBicicletas()
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

listaTVs = []
listaConsolas = []
listaScooters = []
listaBicicletas = []

menu()