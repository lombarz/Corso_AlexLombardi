import random
import numpy as np

casuali=np.random.randint(10,51,(20,))
print("L'array originale con 20 numeri casuali tra 10 a 50 è ",casuali)
firstx_cas=casuali[:10]
print("di cui i primi 10 elementi sono ",firstx_cas)
lastv_cas=casuali[-5:]
print("e gli ultimi 5 ",lastv_cas)
middle_cas=casuali[5:15]
print("gli elementi dal quinto al quattordicesimo sono:" ,middle_cas)
terzi=casuali[2::3]
print("gli elementi in posizione multipla di tre sono", terzi)
casuali[5:10]=99
print("e ora abbiamo cambiato i suoi elementi dal quinto al nono con 99, guarda:", casuali)