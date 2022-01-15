# метод Зейделя
import numpy as np


matrix = [] 
im = int(input('Введите количество строк матрицы: '))
# ввод расширенной матрицы
for i in range(im):
    matrix.append([float(j) for j in input().split()])

matrix = np.array(matrix)
jm = len(matrix[0][:]) # кол-во столбцов


# делим все на диагональные элементы соответ.-но

for i in range(im):
    matrix[i, :] = - matrix[i, :] / matrix[i, i]
    matrix[i, i] = 0


c = - matrix[:,jm-1]


# для условия сходимости    
massiv_norm_2 = []
def norm_matrix_2():
    for i in range(im):
        norm_inf = 0
        for j in range(jm-1):
            norm_inf += abs(matrix[i][j])
        massiv_norm_2.append(norm_inf)
    return max(massiv_norm_2)

massiv_norm_B = []
def norm_matrix_B():
    for i in range(im):
        for j in range(jm-1):
            if j>i:
                massiv_norm_B.append(abs(matrix[i][j]))
    return max(massiv_norm_B)

e = pow(10,-3)  
e1 = ((1-norm_matrix_2())/norm_matrix_B()) * e



result = np.zeros(im)
x0=np.zeros(im, dtype = np.float64) #предыдущее
x=np.zeros(im, dtype = np.float64) #следующее


norm_x = [0]
count = 0 # считает кол-во итераций

if abs(norm_matrix_2())<1:
    while True:    
        for i in range(im):
            for j in range(im):
                if i<j :
                    x[i] += matrix[i,j] *x0[j]   
                else:
                    x[i] += matrix[i,j] *x[j]
            x[i]+=c[i]
        
        count+=1
        result=np.append(result,x,axis=0)  
        norm_x += [(max(abs(x-x0)))]
        if max( abs( x - x0 ) ) < e1:
            print('кол-во итераций = ', count)
            print(x0)
            break
        else:
            x0 = x
            x = np.zeros(im, dtype = np.float64)
            
