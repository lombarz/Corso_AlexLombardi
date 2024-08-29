#programma per modificare frasi
stringa = input("Inserisci una frase")
chc = int(input("Cosa fare con questa frase? 1= aggiungere una parola, 2= rimuovi parola, 3= cambia parola"))
if chc==1:
    new= input("Che parola vuoi aggiungere?")
    stringa = stringa + " " + new 
    print("La tua frase è: ", stringa, ".")
elif chc==2:
    delt = input("che parola vuoi rimuovere?")
    if delt in stringa:
     stringa= stringa.replace(delt, "")
     print("La tua frase è: ", stringa, ".")
    else:
       print("Parola non esistente")
elif chc==3:
    new2 = input("Che parola vuoi aggiungere?")
    delt = input("al posto di quale parola?")
    if delt in stringa:
     stringa= stringa.replace(delt, "")
     print("La tua frase è: ", stringa, ".")
    else:
       print("Parola non esistente")
    stringa= stringa.replace(delt, new2)
    print("La tua frase è: ", stringa, ".")
else:
   print("Scelta non accettata")