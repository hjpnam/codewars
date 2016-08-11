def determinant(matrix):
    output = 0
    if len(matrix) == 1: output += matrix[0][0]
    elif len(matrix) == 2:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        output += a*d-b*c
    else:
        for i in range(len(matrix)):
            output += ((-1) ** i) * determinant(reduceMatrix(matrix,i))
    return output
            
def reduceMatrix(matrix, col):
    reduced = [] 
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            lst = []
            if i != col:
                lst.append(matrix[j][i]) 
            reduced.append(lst)
    del reduced[0]
    return reduced
