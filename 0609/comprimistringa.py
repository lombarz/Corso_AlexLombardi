def decoratore(funzione):
   def avvolgimento(stringa):
      print("Attesa calcoli")
      risultato=funzione(stringa)
      if risultato == stringa:
         print("L'algoritmo di compressione non è efficiente, restituzione stringa originale")
      else:
         print ("Hai cambiato la stringa! Stringa originale: ", stringa)
      return risultato
   return avvolgimento

@decoratore
def comprimi_stringa(stringa):
    stringa+=" "#aggiungo uno spazio in fondo a stringa per togliermi un problema di iterazione sul ciclo for
    stringa2=""
    leng=len(stringa)
    count=1
    for i in range(1,leng):#così il ciclo for è pù semplice
      if stringa[i]==stringa[i-1]:
        count+=1
      else:
         stringa2+=stringa[i-1]+f"{count}"
         count=1
    stringa= stringa[:-1]#rimuovo lo spazio aggiunto
    if len(stringa2)>=leng:
       return stringa
    else:
       return stringa2 
    

frase=input("Inserisci stringa di caratteri: ")
print(comprimi_stringa(frase))