#blocco if else che simula un sistema di login
nome= "alex"# nome predefinito
password= "accipigna"# password predefinita
nomeut=input("quale è il tuo nome?")# prima scelta nome utente
passut= input("Quale è la tua password?")# prima scelta password utente
if nomeut != nome:# primo caso, nome utente sbagliato, registro utente
   print("Utente sconosciuto, registrarsi")
   nomeut = input("nome utente:")
   nome = nomeut
   passut= input("inserisci la tua password")
   password = passut
   print("Le tue credenziali sono nomeutente:"+nome+" password "+ password)
elif nomeut == nome and passut != password:# secondo caso, nome utente giusto, password errata, chiedo di reimpostarla
   risp1=input("Password errata, vuoi reimpostarla?s n")
   if risp1=="s":
      passut= input("inserisci la tua nuova password")
      password = passut
      print("Le tue credenziali sono nomeutente:"+nome+" password "+ password)
   elif risp1=="n":
    print("Utente sconosciuto")
   else:
      print("Scelta non consentita")
else:#terzo caso, credenziali giuste, chiedo se le voglia reimpostare
   risp= input("Benvenuto! Vuoi cambiare le tue credenziali? s n")
   if risp=="s":
      print("Inserire nuove credenziali")
      nomeut = input("nome utente:")
      nome = nomeut
      passut= input("inserisci la tua password")
      password = passut
      print("Le tue credenziali sono nomeutente:"+nome+" password "+ password)
   elif risp=="n":
    print("Le tue credenziali sono nomeutente:"+nome+" password "+ password)
   else:
      print("Scelta non consentita")