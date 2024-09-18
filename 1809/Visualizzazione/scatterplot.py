import matplotlib.pyplot as plt
import numpy as np
x=np.random.rand(50)
y=np.random.rand(50)
plt.figure()#crea figura su cui disegnare il grafico
plt.scatter(x,y)
plt.title("Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()