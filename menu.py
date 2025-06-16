from colorama import Fore
import os , EquiposDeLaboratorio, Inventario,exportar
from Inventario import matriz
from EquiposDeLaboratorio import Equipos
from datetime import datetime
def menu():
    os.system("cls")
    print(Fore.BLUE+"\t --------------------------------")
    print("\t[ MENU del inventario de equipos ]")
    print("\t --------------------------------")
    print(Fore.YELLOW+"\t1 -📋 Ver inventario ")
    print(Fore.BLUE+"\t --------------------------------")
    print(Fore.GREEN+"\t2 -📑 Mostrar equipos")
    print("\t3 -➕ Agregar nuevos equipos")
    print("\t4 -✍🏻 Editar equipo del inventario")
    print("\t5 -🗑️  Eliminar equipo del inventario")
    print("\t6 -🔎 Buscar por equipo ")
    print("\t --------------------------------")
    print(Fore.MAGENTA+"\t7 -📦 Agregar equipos al inventario")
    print("\t8 -🔎 Buscar por equipo ")
    print("\t9 -✍🏻 Editar equipo del inventario")
    print("\t10 -🗑️  Eliminar equipo del inventario")
    print(Fore.YELLOW+"\tS -🛠️ ver inventario malos ")
    print(Fore.YELLOW+"\tS -💾 Salir del programa y Guardar inventario actual")
    print(" --------------------------------")

#main
tamaño=0
while True:
    menu()
    Hora=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    try:
        print(" ---------------------------------------")
        OpcionMenu=input(Fore.BLUE+"Selecciona una opcion >>> ")
        print(" ---------------------------------------")
        if (OpcionMenu=="1"):
            print("Has seleccionado la opcion 1")
            if matriz==[]:
                print("No hay datos en el matriz")
            else:
                print("Los datos del matriz son:")
                print("--------------------------------------------------------")
                Inventario.mostrarmatriz(matriz)
                print("--------------------------------------------------------")
            input("Pulsa una tecla para continuar")

        elif OpcionMenu=="2":
            print("")
            print("Has seleccionado la opcion 2")
            EquiposDeLaboratorio.mostrarEquipo(Equipos)
            input("Pulsa una tecla para continuar")
        elif OpcionMenu=="3":
            print("")
            print("Has seleccionado la opcion 2")
            Equipos=EquiposDeLaboratorio.nuevoEquipo(Equipos)
            input("Pulsa una tecla para continuar")

        elif OpcionMenu=="4":
            print("")
            print("Has seleccionado la opcion 3")
            EquiposDeLaboratorio.editarEquipo()
            input("Pulsa una tecla para continuar")

        elif OpcionMenu=="5":
            print("")
            print("Has seleccionado la opcion 4")
            EquiposDeLaboratorio.eliminarEquipo()
            input("Pulsa una tecla para continuar")

        elif OpcionMenu=="6":
            print("")
            print("Has seleccionado la opcion 2")
            EquiposDeLaboratorio.buscarEquipo(input("Ingrese el equipo a buscar >>> "),Equipos)
            input("Pulsa una tecla para continuar")

        elif OpcionMenu=="7":
            print("")
            print("Has seleccionado la opcion 2")
            print("-----------------------------")
            tamaño=int(input("Ingrese la cantidad de elementos >>> "))
            print("-----------------------------")
            matriz=Inventario.cargar_datos(tamaño,matriz)
            print("- Matriz cargada correctamente")
            Inventario.mostrarmatriz(matriz)
            input("Pulsa una tecla para continuar")

        elif OpcionMenu=="8":
            print("")
            print("Has seleccionado la opcion 4")
            element=input("Ingrese el codigo del equipo a buscar >>> ")
            print(Inventario.buscarElemento(element,matriz))
            input("Pulsa una tecla para continuar")

        elif OpcionMenu=="9":
            print("")
            print("Has seleccionado la opcion 5")
            matriz=Inventario.Editar(matriz)
            Inventario.mostrarmatriz(matriz)
            input("Pulsa una tecla para continuar")
        elif OpcionMenu=="10":
            print("")
            print("Has seleccionado la opcion 5")
            matriz=Inventario.eliminar(matriz)
            input("Pulsa una tecla para continuar")
        elif OpcionMenu=="11":
            print("")
            print("Has seleccionado la opcion 11")
            matrizMala=Inventario.Equiposmalos(matriz)
            Inventario.mostrarmatriz(matrizMala)
            imprimir= input("deseas guardar la matriz? (S/N) >>> ")
            if imprimir.upper()== "S":
                exportar.guardar_matriz_txt(f"{Hora}_EquiposMalos.txt",matrizMala)
                print(Fore.GREEN+"✅ Matriz de equipos malos guardada correctamente")
            else:
                print(Fore.YELLOW+"⚠️ No se guardo la matriz de equipos malos")
            input("Pulsa una tecla para continuar")
            
        elif OpcionMenu=="S":
            exportar.guardar_matriz_txt(f"{Hora}_inventario_guardado.txt", matriz)
            print(Fore.CYAN + "👋 ¡Hasta luego!")
            break
        else:
            print("")
            input("No has pulsado correctamente\n pulsa una tecla para continuar")
    except Exception as e:
        print(Fore.RED + f"⚠️ Error inesperado: {e}")
        input("Pulsa una tecla para continuar")