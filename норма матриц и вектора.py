import numpy as np

# для вектора
def norm_vector():
    vector = list(map(float, input('Введите вектор: \n').split()))
    nv = len(vector)
    norm_1 = 0
    norm_2 = 0
    norm_inf = 0
    for i in range(nv):
        norm_1 += abs(vector[i])
        norm_2 += (vector[i])**2
        if abs(vector[i])>norm_inf:
            norm_inf = abs(vector[i])
    print('Норма 1: ', round(norm_1,2))
    print('Норма 2: ', (norm_2)**0.5)
    print('Норма оо: ', norm_inf)


# для матрицы
def norm_matrix():
    matrix = [] 
    im = int(input('Введите количество строк: '))

    for i in range(im):
        matrix.append([float(j) for j in input().split()])

    matrix = np.array(matrix)
    jm = len(matrix[0][:]) # кол-во столбцов


    massiv_norm_2 = []
    def norm_matrix_2():
        for i in range(im):
            norm_inf = 0
            for j in range(jm):
                norm_inf += abs(matrix[i][j])
            massiv_norm_2.append(norm_inf)

    massiv_norm_1 = []
    def norm_matrix_1():
        for j in range(im):
            norm_1 = 0
            for i in range(jm):
                norm_1 += abs(matrix[i][j])
            massiv_norm_1.append(round(norm_1, 1))


    norm_matrix_1()
    print('Норма 1:', max(massiv_norm_1))
    norm_matrix_2()
    print('Норма 2:', max(massiv_norm_2))
    print(len(matrix[:][0]))    
# norm_matrix()


        
        
        
        
        
        