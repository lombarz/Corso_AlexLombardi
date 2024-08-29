numeri=[]
while True:
 q= int(input("Scegli un numero: "))
 if q > 1:
    for i in range(2, int(q / 2) + 1):
        if (q % i) == 0:
            print("Hai scelto un non primo")
            break
    else:
        print("Hai scelto un numero primo")
        numeri.append(q)

 else:
    print("Hai scelto un numero non primo (=<1)")
 if len(numeri)==5:
  print("Hai scritto cinque numeri primi")
  break