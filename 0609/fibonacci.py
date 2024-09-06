def Fibonacci(numero):
 k='True'
 i=1
 j=0
 z=0
 print("La sequenza di fibonacci fino a ",numero," è: ")
 while k=='True':
  print(i)
  z=i
  i+=j
  j=z
  if numero<i:
   break
 
select=int(input("Inserisci un numero: "))
Fibonacci(select)


