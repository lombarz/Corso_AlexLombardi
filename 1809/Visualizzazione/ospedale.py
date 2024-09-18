import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Parametri della distribuzione
media = 1200          # media visitatori
dev_standard = 900     # deviazione standard 
tendenza = -1.5          # pendenza del trend lineare
distribuzione = {}

inizio = datetime.date(2023, 1, 1)
# Creazione della distribuzione normale
data = []
for n in range(365):
    giorno_corrente = inizio + datetime.timedelta(days=n-1)
    if (n+1)%7==0 or n==358 or n==0 or n==364 or n==127 or n==1 or n==2 or n==3 or n==4:#tolgo un giorno di riposo a settimana(52),4 giorni di ferie natale, capodaano, ultimo dell'anno e un patrono
        continue
    else:
      trend_lineare = n * tendenza  # Creazione di un trend lineare
      vis_randomici = np.random.normal(loc=media, scale=dev_standard)
      visitatori=vis_randomici+trend_lineare
      vis_intero = int(round(visitatori))
      if vis_intero <0:
          vis_intero=0
      ossa=np.random.randint(0,vis_intero+1)
      cuore= np.random.randint(0,vis_intero+1-ossa)
      testa=np.random.randint(0,vis_intero+1-ossa-cuore)
      distribuzione = {"giorno": giorno_corrente, "pazienti": vis_intero,"ossa":ossa,"cuore":cuore,"testa":testa}
      data.append(distribuzione)

# Creare un DataFrame con i dati generati
df = pd.DataFrame(data)
# Assicurarsi che la colonna 'giorno' sia di tipo datetime
df['giorno'] = pd.to_datetime(df['giorno'])
# Calcolare la media mensile dei visitatori
# Raggruppare i dati per mese e calcolare la somma dei visitatori
df_mensile = df.resample('ME', on='giorno').sum()

# Calcolo della media mensile e della deviazione standard
media_mensile = df_mensile['pazienti'].mean()
dev_std_mensile = df_mensile['pazienti'].std()
print("Media mensile dei pazienti:", media_mensile)
print("Deviazione standard mensile dei pazienti:", dev_std_mensile)
conolonne_considerate=df_mensile[["ossa","cuore","testa"]]
colonna_massimo = conolonne_considerate.idxmax(axis=1)
df_mensile["Patologia del mese"]=colonna_massimo
df_mensile.to_csv("Pazienti_mensili",index=True)

plt.figure()#crea figura su cui disegnare il grafico
plt.plot(df["giorno"],df["pazienti"])
plt.title("pazienti per giorno")
plt.xlabel("giorno")
plt.ylabel("pazienti")
plt.show()

df['media_mobile'] = df['pazienti'].rolling(window=7).mean()#rolling serve a riarrangiare un dataframe con un set temporale 

# Creare il grafico a linee dei visitatori giornalieri e della media mobile
plt.figure(figsize=(10, 6))
plt.plot(df['giorno'], df['pazienti'], label='pazienti giornalieri', color='b', alpha=0.5)
plt.plot(df['giorno'], df['media_mobile'], label='Media mobile 7 giorni', color='r', linewidth=2)
plt.title('Pazienti giornalieri con media mobile a 7 giorni', fontsize=16)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Numero di pazienti', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show() 

mesi=["Gen","Feb","Mar","Apr","Mag","Giu","Lug","Ago","Set","Ott","Nov","Dic"]
plt.figure()#crea figura su cui disegnare il grafico
plt.plot(mesi,df_mensile["pazienti"])
plt.title("Grafico pazienti mensili")
plt.xlabel("Mese")
plt.ylabel("Pazienti")
plt.show()

plt.figure()
plt.plot(mesi, df_mensile["ossa"], label="ossa", color='b')  
plt.plot(mesi, df_mensile["testa"], label="testa", color='g') 
plt.plot(mesi, df_mensile["cuore"], label="cuore", color='r') 

# Aggiungere titolo, etichette e legenda
plt.title("Grafico patologie per mese")
plt.xlabel("mese")
plt.ylabel("numero patologie")
plt.legend()  # Mostra la legenda per identificare ogni linea

# Mostrare il grafico
plt.show()
