def decoratore(funzione):
   def avvolgimento(*args):
      print("Attesa calcoli")
      risultato=funzione(*args)
      if risultato == args:
         print("L'algoritmo di compressione non è efficiente, restituzione stringa originale")
      else:
         print ("Hai cambiato la stringa! Stringa originale: ", args)
      return risultato
   return avvolgimento

@decoratore
def comprimi_stringa(stringa):
    stringa2=""
    leng=len(stringa)
    count=1
    for i in range(1,leng):
      if stringa[i]==stringa[i-1]:
        count+=1
      else:
         stringa2+=stringa[i-1]+f"{count}"
         count=1
    if stringa[leng-1]!=stringa[leng-2]:
        stringa2+=stringa[leng-1]+"1"
    else:
       count=1
       for i in range(leng-1,0,-1):
         if stringa[i]==stringa[i-1]:
           count+=1
         else:
           stringa2+=stringa[i]+f"{count}"
           break
    if len(stringa2)>=leng:
       return stringa
    else:
       return stringa2
frase=input("Inserisci frase: ")
print(comprimi_stringa(frase))