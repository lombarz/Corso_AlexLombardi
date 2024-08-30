parole = []
while True:
  new=input("Inserisci una parola: " )
  parole.append(new)
  f=""
  f=input("Vuoi aggiungere un'altra parola? s n ")
  if f=="n":
    print(parole)
    break