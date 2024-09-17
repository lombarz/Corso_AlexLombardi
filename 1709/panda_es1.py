import pandas as pd
import random
import numpy as np

def genera_dati(lista):
    lista_nomi=['Sara','Valerio',""]
    lista_citta=['Bologna','Milano',""]
    nome_casuale = random.choice(lista_nomi)
    citta_casuale = random.choice(lista_citta)
    salario=random.randint(10000,100000)
    eta=random.randint(1,100)
    dizionario={"nome":nome_casuale,"città": citta_casuale,"età":eta,"salario annuo":salario}
    lista.append(dizionario)




dati=[]
print("Benvenuto, iniziamo a creare il database")
for i in range(101):
    genera_dati(dati)
dizionario_fake={"nome":"pippo","città": "corneto","età":1,"salario annuo":np.nan }  
dizionario_fake2={"nome":"paperino","città": "cavola","età":np.nan,"salario annuo":100}
dati.append(dizionario_fake)  
dati.append(dizionario_fake2) 
df=pd.DataFrame(dati)
print("prime 5 righe:\n",df.head(5))
print("ultime 5 righe:\n",df.tail(5))
df['salario annuo'].fillna(df['salario annuo'].median(),inplace=True)
df['età'].fillna(df['età'].median(),inplace=True)
df['nome'].fillna(df['nome'].mode()[0],inplace=True)
df['città'].fillna(df['città'].mode()[0],inplace=True)
df['giovane']=df["età"]<18
df['adulto']=df["età"]>=18
df['senior']=df['età']>65
df.to_csv("data_people_sporchi.csv",index=False)
tipi_di_dato = df.dtypes
print(tipi_di_dato)
df_no_dup=df.drop_duplicates()
print("dataframe origniale \n",df)
print("dataframe senza duplicati\n",df_no_dup)
df_no_dup.to_csv("data_people.csv",index=False)