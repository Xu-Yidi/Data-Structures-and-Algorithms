def matrixElementsSum(matrix):
    index0 = []
    for i in range(0, len(matrix)): #floor
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 0:
                index0.append((i,j))
    result = 0
    for i in range(0, len(matrix)): #floor
        for j in range(0, len(matrix[0])):
            if add_or_not(index0,i,j) is True:
                result = result+matrix[i][j]
    return result
    
def add_or_not(index, i, j):
    floor = [i[0] for i in index]
    room = [i[1] for i in index]
    
    if j in room and i >= floor[room.index(j)]:
        return False
    else:
        return True
