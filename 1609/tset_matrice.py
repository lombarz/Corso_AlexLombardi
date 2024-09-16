import random
import numpy as np
array=np.linspace(0,1,12)
print("L'array è",array)
matrice_uno=array.reshape((3,4))
print("diventa la matrice", matrice_uno)
matrice_due= np.random.rand(3,4)
print("La seconda matrice casuale è", matrice_due)
somma=np.sum(matrice_uno)+np.sum(matrice_due)
print("La somma delle matrici é", somma)
