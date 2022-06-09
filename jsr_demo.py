import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,101)
y = 5*x**2-12*x+7

plt.scatter(x,y,color='r',alpha=0.6)
plt.show
