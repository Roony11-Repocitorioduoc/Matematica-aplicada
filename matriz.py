def sumaMatrices(filas, columnas, Matriz1, Matriz2):
    
    matrizResultado = []
    
    for fila in range(filas):
        
        filaResultado = []
        
        for columna in range(columnas):
            filaResultado.append(round(Matriz1[fila][columna]+Matriz2[fila][columna], 1))
        
        matrizResultado.append(filaResultado)
        
    return matrizResultado
    
def imprimirMatriz(Matriz):
    for fila in range(len(Matriz)):
        print(f"{Matriz[fila]}")
        
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