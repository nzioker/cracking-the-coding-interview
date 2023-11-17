def matrix_rotate(matrix):
    matrix_height = len(matrix) # finding the height of a matrix
    matrix_length = len(matrix[0]) # finding the length of the matrix(number of items in the list contained in the main list)
    new_matrix = [[0]*matrix_height for i in range(matrix_length)] # creating an empty matrix with zeros
    for i in range(matrix_length):
        for j in range(matrix_height):
            new_matrix[j][matrix_height-i-1] = matrix[i][j] 

    return new_matrix

if __name__ == '__main__':
    matrix_one = [[1,2,3],[4,5,6],[7,8,9]]
    print(matrix_rotate(matrix_one))
