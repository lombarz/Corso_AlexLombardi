while True:
 q= int(input("Scegli un numero: "))
 for num in range(q,-1,-1):
  print(num)
 z= input("Vuoi ripetere il countdown con un altro numero? s n ")
 if z=="n":
  break
