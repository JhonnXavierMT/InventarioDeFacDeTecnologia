from colorama import Fore, Back, Style
import os ,random
matriz = [
    ["Cod-1", "NOMBRE", "FUENTE DC", "ESTADO", "Disponible✅", "DETALLE", "Ninguno"],
    ["Cod-2", "NOMBRE", "FUENTE DC", "ESTADO", "Dañado    ❌", "DETALLE", "No prende"],
    ["Cod-3", "NOMBRE", "FUENTE DC", "ESTADO", "Dañado    ❌", "DETALLE", "Corto Circuito"],
    ["Cod-4", "NOMBRE", "FUENTE DC", "ESTADO", "Disponible✅", "DETALLE", "Ninguno"],
    ["Cod-5", "NOMBRE", "FUENTE DC", "ESTADO", "Dañado    ❌", "DETALLE", "Lectura inestable"],
    ["Cod-6",  "NOMBRE", "FUENTE AC",             "ESTADO", "Disponible✅", "DETALLE", "Ninguno"],
    ["Cod-7",  "NOMBRE", "IMPRESORA 3D",          "ESTADO", "Dañado    ❌", "DETALLE", "Error de extrusión"],
    ["Cod-8",  "NOMBRE", "ESCANER",               "ESTADO", "Disponible✅", "DETALLE", "Ninguno"],
    ["Cod-9",  "NOMBRE", "PROYECTOR",             "ESTADO", "Dañado    ❌", "DETALLE", "Lámpara quemada"],
    ["Cod-10", "NOMBRE", "OSCILOSCOPIO",          "ESTADO", "Disponible✅", "DETALLE", "Ninguno"],
    ["Cod-11", "NOMBRE", "OSCILOSCOPIO DIGITAL",  "ESTADO", "Dañado    ❌", "DETALLE", "Pantalla no responde"],
    ["Cod-12", "NOMBRE", "MULTIMETRO",            "ESTADO", "Disponible✅", "DETALLE", "Ninguno"],
    ["Cod-13", "NOMBRE", "GENERADOR DE SEÑALES",  "ESTADO", "Dañado    ❌", "DETALLE", "Distorsión de señal"],
    ["Cod-14", "NOMBRE", "CÁMARA TERMOGRÁFICA",   "ESTADO", "Disponible✅", "DETALLE", "Ninguno"],
    ["Cod-15", "NOMBRE", "ANALIZADOR LÓGICO",     "ESTADO", "Dañado    ❌", "DETALLE", "Conectores rotos"]
]

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

def generar_codigo(i):
    codigo = i+"-"
    for i in range(5):
        codigo += str(random.randint(0, 9))
    return codigo

def cargar_datos(long,matrix):
    for i in range(long):
        list=[]
        for j in range(7):
            if j==0:
                codigo="Cod-"+str(i)
                list.append(codigo)
            elif j==1:
                list.append("NOMBRE")
            elif j==2:
                while True:
                    print
                    ("--------------------------")
                    print("\t[⚡ Opciones de equipos]")
                    for k, equipo in enumerate(Equipos, start=1):
                        print(f"\t{k} - {equipo}")
                    print("--------------------------")
                    print(f"📋 Seleccione el equipo {i} (1-{len(Equipos)}) >>> ", end="")
                    nombre=int(input(f" 📋 ingrese el equipo que quiere >>> "))
                    print("--------------------------")
                    if 1>=nombre or nombre<=len(Equipos):        
                        break
                    else:
                        print("El Equipo no esta en la lista, intente de nuevo.")
                nombre=Equipos[nombre-1]
                list.append(nombre)
            elif j==3:
                list.append("ESTADO")
            elif j==4:
                while True:
                    print("\t[⚡ Opciones de estado]")
                    print("\t1 - Disponible ✅ ")
                    print("\t2 - Dañado ❗")
                    print("--------------------------")
                    estado=int(input("ingrese el estado del equipo >>> "))
                    print("--------------------------")
                    if estado==1:
                        estado="Disponible✅"
                        list.append(estado)
                        break
                    elif estado==2:
                        estado="Dañado    ❌"
                        list.append(estado)
                        break
                    else:
                        print("Estado no valido, intente de nuevo.")
            elif j==5:
                list.append("DETALLE")
            elif j==6:
                print("--------------------------")
                detalle=input("👀 ingrese el detalle del equipo >>> ")
                print("--------------------------")
                if detalle =="":
                    detalle="No hay detalles"
                list.append(detalle)
        matrix.append(list)
        print("\t[Equipo agregado ✔️ ]")
    return matrix

#----------------------------------------------------------------------------------
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
    dato=input("ingrese el elemento a remplazar >>> ")
    remplazo=input("ingrese el remplazo >>> ")
    for element in Equipos:
        indice+=1
        if dato == element:
            pos=indice
    Equipos.remove(dato)
    Equipos.insert(pos,remplazo)
    print(Equipos)

def eliminarEquipo():
    dato=input("ingrese el elemento a remplazar")
    Equipos.remove(dato)
#----------------------------------------------------------------------------------

def mostrarmatriz(matriz):
    print("Los datos del almacen son: ")
    print(Fore.CYAN+"--------------------------------------------------------")
    for fila in matriz:
        for columna in fila:
            if columna == "NOMBRE":
                print(Fore.YELLOW+columna, end=" |")
            elif columna == "ESTADO":
                print(Fore.GREEN+columna, end=" |")
            elif columna == "DETALLE":
                print(Fore.MAGENTA+columna, end=" |")
            else:
                if columna.startswith("Cod-"):
                    print(Fore.BLUE+columna, end=" |")
                else:
                    print(Fore.WHITE+columna, end=" |")
        print("")
    print("--------------------------------------------------------")

def buscarElemento(dato,matriz):
    for fila in matriz:
        for columna in fila:
            if ("Cod-"+dato) == columna:
                return fila
            
def Editar(matriz):
    col=-1
    fil=-1
    indiceFil=0
    indiceCol=0
    dato=input("ingrese el codigo del elemento a editar")
    print("--------------------------------------------------------")
    print("Los datos del almacen son: ")
    print(Fore.GREEN+"",buscarElemento(dato,matriz))
    print("--------------------------------------------------------")
    while True:
        print(Fore.GREEN+"seleccione el campo a editar")
        print("1\t - NOMBRE")
        print("2\t - ESTADO")
        print("3\t - DETALLE")
        print("--------------------------------------------------------")
        campo=int(input("seleccione el campo a editar"))# nombre 
        if campo==1 or campo==2 or campo==3:
            if campo==1:
                campo="NOMBRE"
            elif campo==2:
                campo="ESTADO"
            elif campo==3:
                campo="DETALLE"
            break
        else:
            print(Fore.RED+"Campo no valido, intente de nuevo.")
    if campo == "ESTADO":
        print(Fore.BLACK+"Seleccione el nuevo estado")
        print("1\t - Disponible ✅ ")
        print("2\t - Dañado ❗")
        print("--------------------------------------------------------")
        while True:
            estado=int(input("ingrese el nuevo estado del equipo >>> "))
            if estado==1:
                estado="Disponible✅"
                break
            elif estado==2:
                estado="Dañado    ❌"
                break
            else:
                print(Fore.RED+"Estado no valido, intente de nuevo.")
        for fila in matriz:
            fil+=1
            for columna in fila:
                col+=1
                if "Cod-"+dato == columna:
                    indiceFil=fil
                if campo == columna:
                    indiceCol=col+1
            col=-1
        print("fila>> ",indiceFil,"colum>> ",indiceCol)
        matriz[indiceFil][indiceCol]=estado
    else:
        print("--------------------------------------------------------")
        remplazo=input("ingrese el remplazo") # watimetro
        print("--------------------------------------------------------")
        for fila in matriz:
            fil+=1
            for columna in fila:
                col+=1
                if "Cod-"+dato == columna:
                    indiceFil=fil
                if campo == columna:
                    indiceCol=col+1
            col=-1
        print("fila>> ",indiceFil,"colum>> ",indiceCol)
        matriz[indiceFil][indiceCol]=remplazo
    print(matriz[indiceFil][indiceCol])
    print("DATO EDITADO CORRECTAMENTE ✔️")
    return matriz

def eliminar(matriz):
    fil=-1
    indiceFil=0
    print("--------------------------------------------------------")
    dato=input("ingrese el codigo del elemento a Eliminar")
    print("--------------------------------------------------------")
    print("Elemento seleccionado es: ")
    print(Fore.GREEN+"",buscarElemento(dato,matriz))
    print("Seguro que quiere eliminar este elemento? (S/N)")
    print("--------------------------------------------------------")
    opcion=input("Ingrese la opcion >>> ").strip().upper()
    print("--------------------------------------------------------")
    if opcion == "S":
        for fila in matriz:
            fil+=1
            for columna in fila:
                if "Cod-"+dato == columna:
                    indiceFil=fil
        del matriz[indiceFil]
        print("DATO ELIMINADO CORRECTAMENTE ✔️")
        return matriz
    else:
        print("ELIMINACION CANCELADA. ✔️")
        return matriz
    
    
def menu():
    os.system("cls")
    print(Fore.BLUE+"\t --------------------------------")
    print("\t[ MENU del inventario de equipos ]")
    print("\t --------------------------------")
    print("\t1 -📋 Ver inventario ")
    print("\t --------------------------------")
    print(Fore.GREEN+"\t2 -📑 Mostrar equipos")
    print("\t3 -➕ Agregar nuevos equipos")
    print("\t4 -✍🏻 Editar equipo del inventario")
    print("\t5 -🗑️  Eliminar equipo del inventario")
    print("\t6 -🔎 Buscar por equipo ")
    print("\t --------------------------------")
    print(Fore.YELLOW+"\t7 -📦 Agregar equipos al inventario")
    print("\t8 -🔎 Buscar por equipo ")
    print("\t9 -✍🏻 Editar equipo del inventario")
    print("\t10 -🗑️  Eliminar equipo del inventario")
    print(Fore.BLUE+"\tS -🏃🚪 Salir del programa")
    print(" --------------------------------")

#main
tamaño=0
while True:
    menu()
    
    print(" ---------------------------------------")
    OpcionMenu=input(Fore.MAGENTA+"Selecciona una opcion >>> ")
    print(" ---------------------------------------")
    if (OpcionMenu=="1"):
        print("Has seleccionado la opcion 1")
        if matriz==[]:
            print("No hay datos en el matriz")
        else:
            print("Los datos del matriz son:")
            print("--------------------------------------------------------")
            mostrarmatriz(matriz)
            print("--------------------------------------------------------")
        input("Pulsa una tecla para continuar")

    elif OpcionMenu=="2":
        print("")
        print("Has seleccionado la opcion 2")
        mostrarEquipo(Equipos)
        input("Pulsa una tecla para continuar")
    elif OpcionMenu=="3":
        print("")
        print("Has seleccionado la opcion 2")
        Equipos=nuevoEquipo(Equipos)
        print(Equipos)
        input("Pulsa una tecla para continuar")

    elif OpcionMenu=="4":
        print("")
        print("Has seleccionado la opcion 3")
        editarEquipo()
        print(Equipos)
        input("Pulsa una tecla para continuar")

    elif OpcionMenu=="5":
        print("")
        print("Has seleccionado la opcion 4")
        eliminarEquipo()
        print(Equipos)
        input("Pulsa una tecla para continuar")

    elif OpcionMenu=="6":
        print("")
        print("Has seleccionado la opcion 2")
        buscarEquipo(input("Ingrese el equipo a buscar >>> "),Equipos)
        input("Pulsa una tecla para continuar")
        
    elif OpcionMenu=="7":
        print("")
        print("Has seleccionado la opcion 2")
        print("-----------------------------")
        tamaño=int(input("Ingrese la cantidad de elementos >>> "))
        print("-----------------------------")
        matriz=cargar_datos(tamaño,matriz)
        print("- Matriz cargada correctamente")
        mostrarmatriz(matriz)
        input("Pulsa una tecla para continuar")

    elif OpcionMenu=="8":
        print("")
        print("Has seleccionado la opcion 4")
        element=input("Ingrese el codigo del equipo a buscar >>> ")
        print(buscarElemento(element,matriz))
        input("Pulsa una tecla para continuar")

    elif OpcionMenu=="9":
        print("")
        print("Has seleccionado la opcion 5")
        matriz=Editar(matriz)
        mostrarmatriz(matriz)
        input("Pulsa una tecla para continuar")
    elif OpcionMenu=="10":
        print("")
        print("Has seleccionado la opcion 5")
        matriz=eliminar(matriz)
        mostrarmatriz(matriz)
        input("Pulsa una tecla para continuar")
    elif OpcionMenu=="S":
        break
    else:
        print("")
        input("No has pulsado correctamente\n pulsa una tecla para continuar")
