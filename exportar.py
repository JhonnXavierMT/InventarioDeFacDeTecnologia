from colorama import Fore
def guardar_matriz_txt(nombre_archivo, datos):
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for fila in datos:
                archivo.write(",".join(fila) + "\n")
        print(Fore.GREEN + f"✅ Datos guardados correctamente en '{nombre_archivo}'\n")
    except Exception as e:
        print(Fore.RED + f"⚠️ Error al guardar los datos: {e}\n")