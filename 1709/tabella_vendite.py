import pandas as pd
import datetime
import random

def genera_dati_citta(numero,citta):
    lista_prod=['Mouse','Tastiera','pc','monitor']
    prod=random.choice(lista_prod)
    vendita=random.randint(100,500)
    data=datetime.datetime(2024, 9, numero)
    dizionario={"Città":citta,"Giorno":data,"Prodotto":prod,"Vendita":vendita}
    return dizionario

dati=[]
print("Benvenuto, iniziamo a creare il database")
for i in range(1,31):
    try:
      dati.append(genera_dati_citta(i,"Roma"))
      dati.append(genera_dati_citta(i,"Bologna"))
      dati.append(genera_dati_citta(i,"Milano"))
    except:
      print("Lo sviluppatore è stupido")
df=pd.DataFrame(dati)
pivot_df=df.pivot_table(values='Vendita',index='Prodotto',columns='Città',aggfunc='mean')
gropud_df=df.groupby('Prodotto')['Vendita'].sum()
print("df\n",df)
print("pivot\n",pivot_df)
print("group\n",gropud_df)
