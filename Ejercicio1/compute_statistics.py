"""Ejercicio 1: Estadísticas descriptivas.

Lee un archivo de texto con números (uno por línea) y calcula media, mediana,
moda, varianza y desviación estándar (poblacionales).

Muestra el resultado en consola, lo guarda en StatisticsResults.txt, reporta
líneas inválidas y registra el tiempo de ejecución.
"""

import math
import sys
import time


ARCHIVO_SALIDA = "StatisticsResults.txt"


def leer_numeros(ruta_archivo: str) -> list[float]:
    """Lee números (float) desde un archivo, uno por línea.

    Si una línea es inválida o está vacía, se reporta en consola y se continúa.
    """
    numeros: list[float] = []

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            texto = linea.strip()

            if texto == "":
                print(f"Error en línea {numero_linea}: línea vacía")
                continue

            try:
                numeros.append(float(texto))
            except ValueError:
                print(f"Error en línea {numero_linea}: valor inválido -> {texto}")

    return numeros


def calcular_media(numeros: list[float]) -> float:
    """Calcula la media con un algoritmo básico."""
    suma = 0.0
    for num in numeros:
        suma += num
    return suma / len(numeros)


def calcular_mediana(numeros_ordenados: list[float]) -> float:
    """Calcula la mediana (lista ya ordenada)."""
    n = len(numeros_ordenados)
    mitad = n // 2

    if n % 2 == 0:
        return (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2

    return numeros_ordenados[mitad]


def calcular_moda(numeros: list[float]) -> str:
    """Calcula la moda.

    Regresa la moda si es única; si no existe moda o hay empate, regresa "#N/A".
    """
    frecuencias: dict[float, int] = {}
    for num in numeros:
        frecuencias[num] = frecuencias.get(num, 0) + 1

    max_repeticiones = 1
    moda: float | None = None
    empates = 0

    for valor, repeticiones in frecuencias.items():
        if repeticiones > max_repeticiones:
            max_repeticiones = repeticiones
            moda = valor
            empates = 1
        elif repeticiones == max_repeticiones:
            empates += 1

    if max_repeticiones == 1 or empates > 1:
        return "#N/A"

    return str(moda)


def calcular_varianza_poblacional(numeros: list[float], media: float) -> float:
    """Calcula la varianza poblacional: sum((x-media)^2) / n."""
    suma_varianza = 0.0
    for num in numeros:
        suma_varianza += (num - media) ** 2
    return suma_varianza / len(numeros)


def construir_resultado(datos: dict[str, object]) -> str:
    """Construye el texto de salida del programa.

    Usamos un solo parámetro (diccionario) para mantener el código simple y
    evitar advertencias de pylint por demasiados argumentos.
    """
    return (
        "Statistics Results\n"
        "------------------\n"
        f"COUNT: {datos['cantidad']}\n"
        f"MEAN: {datos['media']}\n"
        f"MEDIAN: {datos['mediana']}\n"
        f"MODE: {datos['moda']}\n"
        f"SD: {datos['desviacion']}\n"
        f"VARIANCE: {datos['varianza']}\n"
        f"ELAPSED_TIME_SECONDS: {datos['tiempo_segundos']}\n"
    )


def escribir_archivo_salida(texto: str) -> None:
    """Escribe el resultado en el archivo requerido."""
    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as salida:
        salida.write(texto)


def main() -> None:
    """Punto de entrada del programa."""
    if len(sys.argv) != 2:
        print("Uso: python computeStatistics.py archivo.txt")
        return

    ruta = sys.argv[1]
    inicio = time.perf_counter()

    try:
        numeros = leer_numeros(ruta)
    except FileNotFoundError:
        print(f"Error: archivo no encontrado -> {ruta}")
        return

    if not numeros:
        print("No hay números válidos para procesar")
        return

    numeros.sort()

    media = calcular_media(numeros)
    mediana = calcular_mediana(numeros)
    moda = calcular_moda(numeros)
    varianza = calcular_varianza_poblacional(numeros, media)
    desviacion = math.sqrt(varianza)

    tiempo_segundos = time.perf_counter() - inicio

    datos_resultado = {
        "cantidad": len(numeros),
        "media": media,
        "mediana": mediana,
        "moda": moda,
        "desviacion": desviacion,
        "varianza": varianza,
        "tiempo_segundos": tiempo_segundos,
    }

    resultado = construir_resultado(datos_resultado)

    print(resultado)
    escribir_archivo_salida(resultado)


if __name__ == "__main__":
    main()
