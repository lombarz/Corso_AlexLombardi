while True:
 num= int(input("Inserisci un numero "))
 if num%2==0:
  print("Il numero è pari")
 else:
  print("Il numero è dispari")
 risp= input("vuoi continuare? s n ")
 if risp== "n":
  break