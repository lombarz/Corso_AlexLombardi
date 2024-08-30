numeri = []
len=0
while True:#ciclo while che fa sia creare l'array e sia conta il numero di elementi
  f=""
  f=input("Vuoi aggiungere un numero? s n ")
  if f=="n":
    break
  else:
   new=int(input("Inserisci un numero: " ))
   numeri.append(new)
   len+=1
if len==0:
  print("La lista è vuota")
# numeri.sort()
# for k in numeri:#questo ciclo for è "finto", ciò che mi fa trovare il numero massimo è sort che me lo mette all'ultimo elemento
#   if k == numeri[len-1]:
#    print("Il valore massimo nella lista è: "+ k)
else:
 max=numeri[0]
 for k in numeri:#ciclo for che determina il valore massimo nella lista
  if k> max:
   max=k
 print("Hai inserito ",len," numeri")
 print("Il valore massimo nella lista è: ",max)
 