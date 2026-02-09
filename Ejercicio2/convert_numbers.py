"""Ejercicio 2: Conversión de números.

Lee un archivo con números enteros y convierte cada uno a binario y
hexadecimal sin usar funciones ni librerías. Muestra los resultados
en consola y los guarda en ConvertionResults.txt.
"""

import sys
import time


ARCHIVO_SALIDA = "ConvertionResults.txt"


def leer_numeros(ruta_archivo: str) -> list[int]:
    """Lee números enteros desde un archivo.

    Las líneas inválidas se reportan y se ignoran.
    """
    numeros: list[int] = []

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            texto = linea.strip()

            if texto == "":
                print(f"Error en línea {numero_linea}: línea vacía")
                continue

            try:
                numeros.append(int(texto))
            except ValueError:
                print(f"Error en línea {numero_linea}: valor inválido -> {texto}")

    return numeros


def convertir_a_binario(numero: int) -> str:
    """Convierte un número entero a binario usando divisiones."""
    if numero == 0:
        return "0"

    resultado = ""
    n = abs(numero)

    while n > 0:
        residuo = n % 2
        resultado = str(residuo) + resultado
        n //= 2

    if numero < 0:
        resultado = "-" + resultado

    return resultado


def convertir_a_hexadecimal(numero: int) -> str:
    """Convierte un número entero a hexadecimal usando divisiones."""
    if numero == 0:
        return "0"

    digitos = "0123456789ABCDEF"
    resultado = ""
    n = abs(numero)

    while n > 0:
        residuo = n % 16
        resultado = digitos[residuo] + resultado
        n //= 16

    if numero < 0:
        resultado = "-" + resultado

    return resultado


def main() -> None:
    """Función principal del programa."""
    if len(sys.argv) != 2:
        print("Uso: python convert_numbers.py archivo.txt")
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

    lineas_resultado: list[str] = []
    encabezado = "DECIMAL | BINARIO | HEXADECIMAL\n"
    lineas_resultado.append(encabezado)

    for numero in numeros:
        binario = convertir_a_binario(numero)
        hexadecimal = convertir_a_hexadecimal(numero)
        linea = f"{numero} | {binario} | {hexadecimal}\n"
        lineas_resultado.append(linea)
        print(linea.strip())

    tiempo = time.perf_counter() - inicio
    lineas_resultado.append(f"\nELAPSED_TIME_SECONDS: {tiempo}\n")

    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as salida:
        salida.writelines(lineas_resultado)


if __name__ == "__main__":
    main()
