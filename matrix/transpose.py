def transpose(matrix):
    
    # Guardo las filas y columnas 
    filas = len(matrix)
    columnas = len(matrix[0])

    # Creo una matriz con datos [0] con tantas columnas como fila tenga y viceversa
    matriz_transpuesta = []
    for _ in range(columnas):
        fila = [0] * filas
        matriz_transpuesta.append(fila)

