"""Ejercicio 3: Conteo de palabras.

Lee un archivo de texto con palabras y cuenta cuántas veces aparece
cada una. Muestra los resultados en consola y los guarda en
WordCountResults.txt, incluyendo el tiempo de ejecución.
"""

import sys
import time


ARCHIVO_SALIDA = "WordCountResults.txt"


def leer_palabras(ruta_archivo: str) -> list[str]:
    """Lee palabras desde un archivo.

    Considera como separadores cualquier whitespace (espacios, tabs, saltos de línea).
    Si una línea está vacía, se reporta el error y se continúa.
    """
    palabras: list[str] = []

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            texto = linea.strip()

            if texto == "":
                print(f"Error en línea {numero_linea}: línea vacía")
                continue

            for token in texto.split():
                palabra = token.strip()
                if palabra == "":
                    print(
                        f"Error en línea {numero_linea}: token vacío en la línea"
                    )
                    continue
                palabras.append(palabra.lower())

    return palabras


def contar_frecuencias(palabras: list[str]) -> dict[str, int]:
    """Cuenta la frecuencia de cada palabra usando un diccionario."""
    frecuencias: dict[str, int] = {}

    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    return frecuencias


def construir_salida(
    nombre_caso: str,
    frecuencias: dict[str, int],
    tiempo_segundos: float,
) -> str:
    """Construye el texto de salida para consola y archivo."""
    lineas: list[str] = [f"Row Labels\tCount of {nombre_caso}\n"]

    for palabra in sorted(frecuencias.keys()):
        lineas.append(f"{palabra}\t{frecuencias[palabra]}\n")

    lineas.append(f"\nELAPSED_TIME_SECONDS\t{tiempo_segundos}\n")

    return "".join(lineas)


def escribir_resultado(texto: str) -> None:
    """Escribe el texto de resultados en el archivo requerido."""
    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as salida:
        salida.write(texto)


def obtener_nombre_caso(ruta_archivo: str) -> str:
    """Obtiene un nombre corto para el encabezado (por ejemplo, TC1)."""
    nombre = ruta_archivo.replace("\\", "/").split("/")[-1]
    if nombre.lower().endswith(".txt"):
        return nombre[:-4]
    return nombre


def main() -> None:
    """Punto de entrada del programa."""
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py fileWithData.txt")
        return

    ruta = sys.argv[1]
    inicio = time.perf_counter()

    try:
        palabras = leer_palabras(ruta)
    except FileNotFoundError:
        print(f"Error: archivo no encontrado -> {ruta}")
        return

    if not palabras:
        print("No hay palabras válidas para procesar")
        return

    frecuencias = contar_frecuencias(palabras)
    tiempo_segundos = time.perf_counter() - inicio

    nombre_caso = obtener_nombre_caso(ruta)
    salida = construir_salida(nombre_caso, frecuencias, tiempo_segundos)

    print(salida)
    escribir_resultado(salida)


if __name__ == "__main__":
    main()
