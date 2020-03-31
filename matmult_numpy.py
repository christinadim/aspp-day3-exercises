# Program to multiply two matrices using nested loops
import numpy as np
# creates matrix
#@profile
def matrix_creator(rows,columns):
    matrix = np.random.randint(0,100, size=(rows, columns))
    return(matrix)
#@profile
def multiplication_of_matrix(matrix1,matrix2):
    if len(matrix1) == len(matrix2):
        matrix3 = np.matmul(matrix1,matrix2)

    else:
        print("the columns of matrix1", len(matrix1)," are different from the rows of matrix2 ", len(matrix2))

    return(matrix3)
N = 250

# NxN matrix
X = matrix_creator(N,N)

# Nx(N+1) matrix
Y = matrix_creator(N,N+1)
result = multiplication_of_matrix(X,Y)
#print("matrix X=\n",X)
#print("matrix Y=\n",Y)
#print("matrix A=\n",a)
for r in result:
    print(r)

###running cProfile on this script shows it takes only 0.318 seconds compared to the intial one which took around 5.8 seconds.
