import random
casual=random.randint(0,100)
chc= 'True'
while chc== 'True':
  guess=int(input("Inserisci il numero da indovinare (0-100)! "))
  if guess==casual:
    print("Indovinato!")
    break
  elif guess<casual:
    chc2=input("Il numero da indovinare è più alto! Vuoi riprovare? s n")
    if chc2== 'n':
       chc='False'
  elif guess>casual:
    chc2=input("Il numero da indovinare è più basso! Vuoi riprovare? s n")
    if chc2== 'n':
       chc='False'