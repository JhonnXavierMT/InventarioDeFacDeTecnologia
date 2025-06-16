from colorama import Fore
def guardar_matriz_txt(nombre_archivo, datos):
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            # Abre (o crea) un archivo con el nombre indicado en 'nombre_archivo' en modo escritura ("w").
            # El parámetro encoding="utf-8" garantiza que se manejen correctamente caracteres especiales (como tildes, eñes, etc.).
            # 'with' asegura que el archivo se cierre automáticamente al finalizar el bloque.

            for fila in datos:
                archivo.write(",".join(fila) + "\n")
                # Une los elementos de la fila separados por comas (",") y le añade un salto de línea al final.
                # Luego, escribe esa línea en el archivo.

        print(Fore.GREEN + f"✅ Datos guardados correctamente en '{nombre_archivo}'\n")
    except Exception as e:
        print(Fore.RED + f"⚠️ Error al guardar los datos: {e}\n")
