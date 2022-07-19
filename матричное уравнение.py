import numpy as np

n = int(input('Введите порядок матрицы: '))
# вычисление минора
def matrix_minor(m, i, j):
    return np.delete(np.delete(m,i,axis=0), j, axis=1)
# определитель для матрицы порядка 2
def det2D(a):
    return a[0][0] * a[1][1] -  a[0][1] * a[1][0]
# определитель для матрицы порядка 3
def triangle_det(a):
    m1, m2 = matrix_minor(a, 0, 0), matrix_minor(a, 0, 1)
    m3 = matrix_minor(a, 0, 2)
    return a[0][0] * det2D(m1) - a[0][1] * det2D(m2) + a[0][2] * det2D(m3)

# матрица алгебраических дополнений
def matrix_algdop(matrix):
    Ad = np.zeros((n,n),dtype = np.int32)
    listfordet = []
    M = 0 # минор i-го элемента - матрица <= 3х стлб. в данной реализации
    for i in range(n):
        for j in range(n):
            M = matrix_minor(matrix,i,j) # каждый раз будет замена переменной
            detM = 0   # для определителя минора
            if len(M)==1:
                detM = M[0][0]
            elif len(M)==2:
                detM = det2D(M) 
            elif len(M)==3:
                detM = triangle_det(M)
            Ad[i][j] = ((-1)**(i+j))*detM
        listfordet.append(Ad[0][i]*matrix[0][i])
    return Ad, listfordet

# пока рассмотрю для n не больше 4
def determinant_matrix(matrix):
    detA = 0 
    if n==1:
        detA = matrix[0]
    elif n==2:
        detA = det2D(matrix)
    
    elif n>2:
        detA = sum(matrix_algdop(matrix)[1])

    return detA
        
# делаю с акцентом на такой формат уравнения: А*X=B
# A^(-1)*A*X=A^(-1)*B

def transpose(matrix):
    def transpose(matrix):
    matrixnew = np.array([list(i) for i in zip(*matrix)])

    return matrixnew

def multiply_matrix(A, B):
    result_matrix = np.zeros((n,n),dtype = np.int32)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result_matrix[i][j] += A[i][k] * B[k][j]
    return result_matrix


def matrix_equation():
    matrix_A , matrix_B = [], []
    print('Введите матрицу A:')
    for i in range(n):
        matrix_A.append([int(j) for j in input().split()])
    print('Введите матрицу B:')
    for i in range(n):
        matrix_B.append([int(j) for j in input().split()])
    
    matrix_A = np.array(matrix_A[::-1], dtype=np.int32)
    matrix_B = np.array(matrix_B[::-1], dtype=np.int32)
    
    M_alg = matrix_algdop(matrix_A)[0]

    print('определитель матрицы:\n', determinant_matrix(matrix_A))
    print('матрица алгебраических дополнений:\n', M_alg )
    print('транспонированная: \n', transpose(M_alg))
    
    SA = (1/determinant_matrix(matrix_A))*(transpose(M_alg))
    
    print('X: \n', multiply_matrix(SA,matrix_B))
 
    
 
matrix_equation()    
    

    
    
    
    
    
    
    
    
    






