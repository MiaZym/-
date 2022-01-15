import numpy as np

n = int(input('Введите порядок матрицы: '))
# matrix = [[5,-2,1],
#          [3,1,-4],
 #         [6,0,-3]]
matrix = [[5,-2,1,2],
         [3,1,-4,3],
         [6,0,-3,1],
         [3,1,2,1]]
matrix = np.array(matrix, dtype=np.int32)
# matrix = [[5,-2],
#          [3,1]]

# ввод матрицы n-го порядка
'''
for i in range(5):
    matrix.append([int(j) for j in input().split()])

'''

# вычисление минора
def matrix_minor(m, i, j):
    return np.delete(np.delete(m,i,axis=0), j, axis=1)

def det2D(a):
    return a[0][0] * a[1][1] -  a[0][1] * a[1][0]

def triangle_det(a):
    m1, m2 = matrix_minor(a, 0, 0), matrix_minor(a, 0, 1)
    m3 = matrix_minor(a, 0, 2)
    return a[0][0] * det2D(m1) - a[0][1] * det2D(m2) + a[0][2] * det2D(m3)

# для определителя (пока рассмотрю для n не больше 4)
detA = 0

if n==1:
    detA = matrix[0]
elif n==2:
    detA = det2D(matrix)
    
elif n>2:
    Ad = [] # массив всех алгебраических дополнений
    M = 0 # минор i-го элемента - матрица <= 3х стлб. в данной реализации
    for i in range(n):
        M = matrix_minor(matrix,0,i) # каждый раз будет замена переменной
        detM = 0   # для определителя минора
        if len(M)==1:
            detM = M[0][0]
        elif len(M)==2:
            detM = M[0][0]*M[1][1]-M[1][0]*M[0][1] 
        elif len(M)==3:
            detM = triangle_det(M)
        Ad.append(((-1)**(i))*matrix[0][i]*detM)
    detA = sum(Ad)                 

print(detA)



    