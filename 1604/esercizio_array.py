import numpy as np

array=np.arange(10,50)
print(array)
print(f"L'array contine dati di tipo {array.dtype}")
array= array.astype(float)
print(f"Ora l'array contine dati di tipo {array.dtype}")
print(f"L'array ha forma {array.shape}")
re_arr=array.reshape((4,10))
print(re_arr)
print(f"L'array ha forma {re_arr.shape}")