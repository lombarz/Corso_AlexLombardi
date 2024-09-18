import matplotlib.pyplot as plt
cat=["A","B","C","D","E"]
val=[1,3,2,7,11]
plt.figure()#crea figura su cui disegnare il grafico
plt.bar(cat,val)
plt.title("Grafico a Barre")
plt.xlabel("Categorie")
plt.ylabel("Valori")
plt.show()