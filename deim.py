
# importing the required module 
import matplotlib.pyplot as plt 
import math as mt
import numpy as np
# x axis values 
x = list(np.arange(-1.,1.,0.001)) 

MI = list(np.arange(1.,mt.pi,0.6)) 

snapshots =[]
for mi in MI:
    y = list(map(lambda x : (1-x)*mt.cos(mt.pi*3*mi*(x+1))*mt.exp(-(1+x)*mi) , x))
    snapshots.append(y)  
    # plotting the points  
    plt.plot(x,y) 

snaps = np.array(snapshots)
u, s, vh = np.linalg.svd(snaps, full_matrices=True)
u.shape, s.shape, vh.shape

# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('A nonlinear parametrized function with spatial points in one dimension.') 
  
# function to show the plot 
plt.show() 
 