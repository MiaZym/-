import numpy as np
import matplotlib.pyplot as plt

x = np.fromfile('x_data.txt',float,sep='\n') 
y = np.fromfile('y_data.txt',float,sep='\n')

L = 0
n = len(x)
xx = np.arange(-5, 5, 0.01)

for i in range(n):
    for j in range(n):
        if j!=i:
            L = np.sum(L, y[i]* np.prod([(x - x[j]) / (x[i] - x[j])], axis=0))




#x1 = np.linspace(0,5.,50)
#f = np.interp(x1,x,y)
plt.scatter(x,y)
вplt.plot(x,L)
plt.show()









