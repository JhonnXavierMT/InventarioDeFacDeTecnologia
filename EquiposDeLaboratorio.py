from colorama import Fore, Style
Equipos = [
    "FUENTE DC", 
    "FUENTE AC", 
    "IMPRESORA 3D", 
    "ESCANER", 
    "PROYECTOR", 
    "OSCILOSCOPIO", 
    "OSCILOSCOPIO DIGITAL", 
    "MULTIMETRO", 
    "GENERADOR DE SEÑALES", 
    "CÁMARA TERMOGRÁFICA", 
    "ANALIZADOR LÓGICO"
]
def nuevoEquipo(list):
    print("--------------------------")
    print("\t[⚡Equipos Existentes]")
    for k, equipo in enumerate(list, start=1):
        print(f"\t{k} - {equipo}")
    print("--------------------------")
    nombre=input("📋 ingrese el nuevo equipo que quiere >>> ")
    print("--------------------------")
    if 0==list.count(nombre):
        list.append(nombre)
        print("El equipo fue gregado. ✔️")
        return list
    else:
        print("El equipo ya existe en la lista, NO se agrego.⚠️")
        return list
def mostrarEquipo(Equipos):
    for dato in Equipos:
        print(dato,end="")
        print("")

def buscarEquipo(dato,Equipos):
    b=False
    for element in Equipos:
        if dato == element:
            b=True
            break
    if b:
        print(Fore.GREEN+"✅ Se logro encontrar el elemento en Equipos", dato)
    else:
        print(Fore.RED+"⚠️ No se logro encontrar el elemento en Equipos", dato)
            
def editarEquipo():
    indice=-1
    pos=0
    while True:
        print(Fore.BLUE+"---------------------------------------------")
        dato=input("ingrese el elemento a remplazar >>> ")
        print("---------------------------------------------")
        if dato not in Equipos or dato== "":
            print(Fore.RED+"⚠️ El elemento no se encuentra en la lista, intente de nuevo.")
            break
        remplazo=input("ingrese el remplazo >>> ")
        print("---------------------------------------------")
        if remplazo in Equipos or remplazo== "":
            print(Fore.RED+"⚠️ El remplazo ya existe en la lista, intente de nuevo.")
            break
        for element in Equipos:
            indice+=1
            if dato == element:
                pos=indice
        Equipos.remove(dato)
        Equipos.insert(pos,remplazo)
        print(Fore.GREEN+"✅ Se logro editar el elemento en Equipos", dato)
        break

def eliminarEquipo():
    dato=input("ingrese el elemento a remplazar")
    if dato not in Equipos or dato== "":
        print(Fore.RED+"⚠️ El elemento no se encuentra en la lista, intente de nuevo.")
        return
    else:
        Equipos.remove(dato)
        print(Fore.GREEN+"---------------------------------------------")
        print("Se elimino ✅ ")
        print("---------------------------------------------")