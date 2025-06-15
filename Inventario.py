import random
from EquiposDeLaboratorio import Equipos
from colorama import Fore, init
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
                    print(f"📋 Seleccione el equipo {i} (1-{len(Equipos)})")
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
        if remplazo=="":
            remplazo="No hay detalles"
        else:
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
    if not buscarElemento(dato, matriz):
        print(Fore.RED+"El elemento no existe en la matriz.⚠️")
        return matriz
    print("Seguro que quiere eliminar este elemento 🤔? (S/N)")
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
  