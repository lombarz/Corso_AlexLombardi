while True:
 q= int(input("Scegli un numero intero positivo: "))
 if q>0:
  for num in range(q,-1,-1):
   print(num)
  z= input("Vuoi ripetere il countdown con un altro numero? s n ")
  if z=="n":
   break
 else:
  z=input("Il numero non è un intero positivo, ripetere? s n")
  if z=="n":
   break