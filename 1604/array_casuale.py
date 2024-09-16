import random
import numpy as np

casuali=np.random.randint(10,50,(20,))
print(casuali)
x_cas=casuali[:10]
print(x_cas)
lastv_cas=casuali[-5:]
print(lastv_cas)
middle_cas=casuali[5:15]
print(middle_cas)
terzo=casuali[2]
print(terzo)
casuali[5:10]=99
print(casuali)
