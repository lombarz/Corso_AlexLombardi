import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Parametri della distribuzione
media = 2000          # media visitatori
dev_standard = 500     # deviazione standard 
tendenza = 2           # pendenza del trend lineare
distribuzione = {}

inizio = datetime.date(2023, 1, 1)
# Creazione della distribuzione normale
data = []
for n in range(365):
    giorno_corrente = inizio + datetime.timedelta(days=n)
    trend_lineare = n * tendenza  # Creazione di un trend lineare
    vis_randomici = np.random.normal(loc=media, scale=dev_standard)
    vis_intero = int(round(vis_randomici))
    distribuzione = {"giorno": giorno_corrente, "visitatori": vis_intero + trend_lineare}
    data.append(distribuzione)

# Creare un DataFrame con i dati generati
df = pd.DataFrame(data)

# Assicurarsi che la colonna 'giorno' sia di tipo datetime
df['giorno'] = pd.to_datetime(df['giorno'])

# Calcolare la media mobile a 7 giorni
df['media_mobile'] = df['visitatori'].rolling(window=7).mean()

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
df_mensile = df.resample('ME', on='giorno').mean()

# Creare un grafico della media mensile dei visitatori
plt.figure(figsize=(10, 6))  # Imposta le dimensioni della figura
plt.plot(df_mensile.index, df_mensile['visitatori'], marker='o', color='g', label='Media mensile')

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