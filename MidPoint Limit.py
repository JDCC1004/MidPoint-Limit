from os.path import exists
import numpy as np

def vector(funcionX, funcionY, funcionZ, t):
    # Definimos las funciones matemáticas comunes que queremos permitir
    numpy_functions = {'sin': np.sin, 'cos': np.cos, 'tan': np.tan, 'exp': np.exp,
                       'log': np.log, 'sqrt': np.sqrt, 'abs': np.abs}

    # Definimos las variables que queremos permitir
    t_value = t

    # Evaluamos las funciones para obtener los valores de x, y, y z
    x = eval(funcionX, {}, {**numpy_functions, 't': t_value})
    y = eval(funcionY, {}, {**numpy_functions, 't': t_value})
    z = eval(funcionZ, {}, {**numpy_functions, 't': t_value})

    return x, y, z

def aproximacionPuntoMedio(funcionX, funcionY, funcionZ, t0, delta, iteracionesMax=1000):
    epsilon = 1e-10  # Tolerancia para la convergencia
    iteraciones = 0
    while iteraciones < iteracionesMax:
        puntoIzqX, puntoIzqY, puntoIzqZ = vector(funcionX, funcionY, funcionZ, t0 - delta / 2)
        puntoDerX, puntoDerY, puntoDerZ = vector(funcionX, funcionY, funcionZ, t0 + delta / 2)
        limiteX = (puntoIzqX + puntoDerX) / 2
        limiteY = (puntoIzqY + puntoDerY) / 2
        limiteZ = (puntoIzqZ + puntoDerZ) / 2

        if abs(limiteX - puntoIzqX) < epsilon and abs(limiteY - puntoIzqY) < epsilon and abs(limiteZ - puntoIzqZ) < epsilon:
            return limiteX, limiteY, limiteZ, iteraciones, True
        delta /= 2
        iteraciones += 1
    return None, None, None, iteraciones, False


def main():
    # Solicitar al usuario que ingrese las funciones
    funcionX = input("Ingrese la función x(t): ")
    funcionY = input("Ingrese la función y(t): ")
    funcionZ = input("Ingrese la función z(t): ")

    # Solicitar al usuario que ingrese el punto a evaluar y el tamaño del intervalo
    t0 = float(input("Ingrese el valor de t0: "))
    delta = float(input("Ingrese el valor de delta (tamaño del intervalo): "))

    # Calcular el límite por aproximación de punto medio
    limiteX, limiteY, limiteZ, iteraciones, existe = aproximacionPuntoMedio(funcionX, funcionY, funcionZ, t0, delta)

    # Imprimir el resultado
    if existe:
        print("Límite de la función vectorial en t0 =", t0, ": <", limiteX, ",", limiteY, ",", limiteZ, ">")
        print("Cantidad de iteraciones:", iteraciones)
    else:
        print("No se pudo encontrar el límite después de", iteraciones, "iteraciones")


if __name__ == "__main__":
    main()
