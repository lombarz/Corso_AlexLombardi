numeri = []
while True:
  new=int(input("Inserisci un numero: " ))
  numeri.append(new)
  f=""
  f=input("Vuoi aggiungere un altro numero? s n ")
  if f=="n":
    break
for k in numeri:
  print(k**2)
