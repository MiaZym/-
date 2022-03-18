import numpy as np
import matplotlib.pyplot as plt


x = np.fromfile('x_data.txt',float,sep='\n') 
y = np.fromfile('y_data.txt',float,sep='\n')

a = (len(x)*np.sum(x*y) - np.sum(x)*np.sum(y))/(len(x)*np.sum(x*x)-np.sum(x)*np.sum(x))
b = (np.sum(y)-a*np.sum(x))/len(x)

y0 = a*x + b

plt.scatter(x, y)
plt.plot(x, y0)
plt.show()

