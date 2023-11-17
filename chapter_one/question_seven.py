#This function creates a new matrix of dimensions mxn and fills them up with zeros
def matrix_former(height, length):

    new_matrix = []
    for i in range(length):
        new_matrix.append([0]*height)
    return new_matrix
    
    
def matrix_former_two(height, length):
    return [[0]*height for i in range(length)]


                


if __name__ == '__main__':
    print(matrix_former(3,4))