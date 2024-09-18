import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_theme(style="darkgrid")#imposta seaborn
data=np.random.normal(size=100)#genera dati secondo la distribuzione normale
sns.histplot(data, kde=True)#Kernel Density Estimate (Stima della Densità del Nucleo)= linea distribuzione di probabilità della variabile continua
plt.title("Distribuzione dei dati")
plt.show()

