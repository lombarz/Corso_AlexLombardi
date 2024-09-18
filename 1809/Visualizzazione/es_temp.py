import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def genera_temperatura_citta(numero):
    temperatura_cas=np.random.normal(15,5)
    temperatura=np.round(temperatura_cas).astype(int)
    #data=datetime.datetime(2024, 9, numero)
    dizionario={"Giorno":numero,"Temperatura":temperatura}
    return dizionario

dati=[]
print("Benvenuto, iniziamo a creare il database")
for i in range(1,31):
  try:
    dati.append(genera_temperatura_citta(i))
  except:
     print("Alex è stupido")

df=pd.DataFrame(dati)
media=df["Temperatura"].mean()
massima=df["Temperatura"].max()
minima=df["Temperatura"].min()
moda=df["Temperatura"].mode()[0]
print(f"Tempratura media: {media}\n Temperatura massima: {massima}\n Temperatura Minima: {minima} \n Moda: {moda}")

plt.figure()#crea figura su cui disegnare il grafico
plt.bar(df["Giorno"],df["Temperatura"])
plt.title("Tempeartura per giorno")
plt.ylabel("Temperatura")
plt.xlabel("Giorno")
plt.legend([f"Media: {media:.2f}, Minimo: {minima:.2f}, Massimo: {massima:.2f}, Moda: {moda:.2f}"])
plt.show()

plt.figure()#crea figura su cui disegnare il grafico
plt.hist(df["Temperatura"],bins=26)
plt.title("Occorrenza Tempearture")
plt.xlabel("Temperatura")
plt.ylabel("Occorrenza")
plt.legend([f"Media: {media:.2f}, Minimo: {minima:.2f}, Massimo: {massima:.2f}, Moda: {moda:.2f}"])
plt.show()

sns.set_theme(style="darkgrid")#imposta seaborn
sns.histplot(df["Temperatura"], kde=True)#Kernel Density Estimate (Stima della Densità del Nucleo)= linea distribuzione di probabilità della variabile continua
plt.title("Distribuzione Temperature")
plt.legend([f"Media: {media:.2f}, Minimo: {minima:.2f}, Massimo: {massima:.2f}, Moda: {moda:.2f}"])
plt.show()

plt.figure()#crea figura su cui disegnare il grafico
plt.scatter(df["Giorno"],df["Temperatura"])
plt.title("Scatter Plot Temperature")
plt.xlabel("Giorno")
plt.ylabel("Temperatura")
plt.legend([f"Media: {media:.2f}, Minimo: {minima:.2f}, Massimo: {massima:.2f}, Moda: {moda:.2f}"])
plt.show()