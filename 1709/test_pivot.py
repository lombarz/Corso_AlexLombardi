import pandas as pd

data={
    'Data':['2021-01-01','2022-02-02','2022-04-12','2022-03-03','2024-04-04'],
    'Città':['Roma','Bologna','Milano','Napoli','Palermo'],
    'Prodotto':['Mouse','Tastiera','Mouse','Tastiera','Mouse'],
    'Vendite':[100,145,200,300,160]
}
df=pd.DataFrame(data)
pivot_df=df.pivot_table(values='Vendite',index='Prodotto',columns='Città',aggfunc='mean')
gropud_df=df.groupby('Prodotto').sum()
print(df)
print(pivot_df)
print(gropud_df)