

# contuor plot

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0.0,20.0,100)
y=np.linspace(0.0,4.0,100)
X,Y=np.meshgrid(x,y)
Z=(20/np.pi)*np.exp(-np.pi*Y/10)*np.sin(2*np.pi*x/10)
plt.contour(X,Y,Z)
plt.show()

