def generarMatriz(filas, escalarI, columnas, escalarJ, operacion):

    matrizResultado = []

    for fila in range(1, filas+1):

        filaResultado = []

        for columna in range(1, columnas+1):
            if operacion==1:
                filaResultado.append(fila*escalarI+columna*escalarJ)
            elif operacion==2:
                filaResultado.append(fila*escalarI*columna*escalarJ)
            else:
                print(f"No manejo esa operación!")
                return 
        
        matrizResultado.append(filaResultado)

    return matrizResultado

def imprimirMatriz(Matriz):
    for fila in range(len(Matriz)):
        print(f"{Matriz[fila]}")

def sumaMatrices(Matriz1, Matriz2):

    filas = len(Matriz1)
    columnas = len(Matriz1[0])

    if (filas != len(Matriz2) and columnas != len(Matriz2[0])):
        print(f"No se pueden sumar esas matrices! Dimensiones Matriz 1: {filas}X{columnas} - Matriz 2: {len(Matriz2)}X{len(Matriz2[0])}")
        return []
    
    matrizResultado = []
    
    for fila in range(filas):
        
        filaResultado = []
        
        for columna in range(columnas):
            filaResultado.append(round(Matriz1[fila][columna]+Matriz2[fila][columna], 1))
        
        matrizResultado.append(filaResultado)
        
    return matrizResultado

def ponderarMatriz(escalar, Matriz):
    filas = len(Matriz)
    columnas = len(Matriz[0])
    
    matrizResultado = []
    
    for fila in range(filas):
        
        filaResultado = []
        
        for columna in range(columnas):
            filaResultado.append(escalar*Matriz[fila][columna])
        
        matrizResultado.append(filaResultado)
    
    return matrizResultado

def transponerMatriz(Matriz):

    filas = len(Matriz)
    columnas = len(Matriz[0])

    matrizTranspuesta = []

    for columna in range(columnas):

        filaTranspuesta = []

        for fila in range(filas):

            filaTranspuesta.append(Matriz[fila][columna])
    
        matrizTranspuesta.append(filaTranspuesta)
    
    return matrizTranspuesta


def multiplicarMatriz(Matriz1, Matriz2):

    filas = len(Matriz1)
    columnas = len(Matriz1[0])

    if (columnas != len(Matriz2)):
        print(f"No se pueden multiplicar esas matrices! Dimensiones Matriz 1: {filas}X{columnas} - Matriz 2: {len(Matriz2)}X{len(Matriz2[0])}")
        return []
    
    filasResultado = filas
    columnasResultado = len(Matriz2[0])

    # Creamos la matriz con tamaño necesario
    matrizResultado = generarMatriz(filasResultado, 0, columnasResultado, 0, 1)

    for filaR in range(filasResultado):
        for columnaR in range(columnasResultado):
            suma = 0
            for columna in range(columnas):
                suma += Matriz1[filaR][columna]*Matriz2[columna][columnaR]

            matrizResultado[filaR][columnaR] = suma

    return matrizResultado

def calcularMatrizReducida(Matriz, i, j):
    
    filas = len(Matriz)
    columnas = len(Matriz[0])
    
    if (i > filas or j > columnas):
        print(f"Index out")
        return []
    
    if (filas == 1 and columnas == 1):
        return Matriz[0][0]
    
    matrizResultado = []
    
    matrizTemporal = Matriz
    
    # Borra la columna j
    for fila in range(filas):
        matrizTemporal[fila].pop(j)
    
    # Borra la fila i
    matrizTemporal.pop(i)
    
    matrizResultado = matrizTemporal
    
    return matrizResultado

def calcularDeterminanteMatriz(Matriz):
    filas = len(Matriz)
    columnas = len(Matriz[0])
    
    if (filas != columnas):
        print(f"Esta matriz no tiene determinante")
        return 0
    
    determinante = 0
    
    for fila in range(filas):
        for columna in range(columnas):
            determinante += (-1)**((fila+columna+2))*calcularMatrizReducida(Matriz, fila, columna)
    
    return determinante

if __name__ == "__main__":
    print(f"Libreria creada en 2024\nRicardo Sánchez")
    
    A = generarMatriz(4, 2, 4, 2, 2)
    
    imprimirMatriz(A)
    
    print(f"{calcularDeterminanteMatriz(A)}")
    
    
    