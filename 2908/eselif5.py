print("Inserisci i due numeri di cui desideri effettuare un'operazione: ")
a= int(input("Primo numero: "))
b= int(input("Secondo numero: "))
chc= int(input("che operazione vuoi effettuare? 1= +, 2= -, 3= *, 4= /"))
if chc==1:
 print(a+b)
elif chc==2:
 print(a-b)
elif chc==3:
 print(a+b)
elif chc==4:
 if b!=0:
  print(a/b)
 else:
  print("Impossibile dividere per 0!")
else:
 print("Scelta non consentita")