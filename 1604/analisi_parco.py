import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Parametri della distribuzione
media = 2000          # media visitatori
dev_standard = 500     # deviazione standard 
tendenza = 0.5           # pendenza del trend lineare
distribuzione = {}

inizio = datetime.date(2023, 1, 1)
# Creazione della distribuzione normale
data = []
for n in range(365):
    giorno_corrente = inizio + datetime.timedelta(days=n)
    trend_lineare = n * tendenza  # Creazione di un trend lineare
    vis_randomici = np.random.normal(loc=media, scale=dev_standard)
    visitatori=vis_randomici+trend_lineare
    vis_intero = int(round(visitatori))
    distribuzione = {"giorno": giorno_corrente, "visitatori": vis_intero}
    data.append(distribuzione)

# Creare un DataFrame con i dati generati
df = pd.DataFrame(data)

# Assicurarsi che la colonna 'giorno' sia di tipo datetime
df['giorno'] = pd.to_datetime(df['giorno'])#non dovrebbe servire

# Calcolare la media mobile a 7 giorni
df['media_mobile'] = df['visitatori'].rolling(window=7).mean()#rolling serve a riarrangiare un dataframe con un set temporale 

# Creare il grafico a linee dei visitatori giornalieri e della media mobile
plt.figure(figsize=(10, 6))
plt.plot(df['giorno'], df['visitatori'], label='Visitatori giornalieri', color='b', alpha=0.5)
plt.plot(df['giorno'], df['media_mobile'], label='Media mobile 7 giorni', color='r', linewidth=2)
plt.title('Visitatori giornalieri con media mobile a 7 giorni', fontsize=16)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Numero di visitatori', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show() 

# Calcolare la media mensile dei visitatori
# Raggruppare i dati per mese e calcolare la somma dei visitatori
df_mensile = df.resample('M', on='giorno').sum()
df_media_mensile = df.resample('M', on='giorno').mean()
print(df_mensile)
print(df_media_mensile)

# Calcolo della media mensile e della deviazione standard
media_mensile = df_mensile['visitatori'].mean()
dev_std_mensile = df_mensile['visitatori'].std()

print("Media mensile dei visitatori:", media_mensile)
print("Deviazione standard mensile dei visitatori:", dev_std_mensile)

media_giorni_mensile = df_media_mensile['visitatori'].mean()
dev_std_giorni_mensile = df_media_mensile['visitatori'].std()


print("Media giornaliera dei visitatori per mese:", media_giorni_mensile)
print("Deviazione standard dei visitatori:", dev_std_giorni_mensile)

# Il metodo df.resample() di pandas è utilizzato per ristrutturare e
# aggregare i dati temporali in un DataFrame secondo una nuova frequenza temporale. 
# Questo metodo è molto utile per lavorare con
# serie temporali e per convertire i dati da una frequenza a un'altra (ad esempio, da dati giornalieri a dati mensili)

# Creare un grafico della media mensile dei visitatori
plt.figure(figsize=(10, 6))  # Imposta le dimensioni della figura
plt.plot(df_mensile.index, df_mensile['visitatori'], marker='o', color='g', label='Visitatori mensili')

# Aggiungere etichette e titolo
plt.title('Media mensile dei visitatori', fontsize=16)
plt.xlabel('Mese', fontsize=12)
plt.ylabel('Numero medio di visitatori', fontsize=12)

# Abilitare la griglia e la legenda
plt.grid(True)
plt.legend()

# Mostrare il grafico della media mensile
plt.tight_layout()
plt.show()

# Creare un grafico della media mensile dei visitatori
plt.figure(figsize=(10, 6))  # Imposta le dimensioni della figura
plt.plot(df_media_mensile.index, df_media_mensile['visitatori'],marker='o', color='g', label='Visitatori medi per mesi')

# Aggiungere etichette e titolo
plt.title('Media giornaliera dei visitatori per mese', fontsize=16)
plt.xlabel('Mese', fontsize=12)
plt.ylabel('Numero medio di visitatori', fontsize=12)

# Abilitare la griglia e la legenda
plt.grid(True)
plt.legend()

# Mostrare il grafico della media mensile
plt.tight_layout()
plt.show()