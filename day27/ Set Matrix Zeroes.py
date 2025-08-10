def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row0 = False

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                if i > 0:
                    matrix[i][0] = 0
                else:
                    row0 = True

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        for i in range(rows):
            matrix[i][0] = 0
