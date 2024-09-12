def lettura_file(nome_testo):
    with open(nome_testo,"r") as myfile:
        return myfile.read()
def scrittura_file(file,stringa):
    with open(file,"a") as myfile:
        myfile.write(stringa)

contenuto =lettura_file("1209/testCsv.txt")

righe = contenuto.split("\n")

print(righe)

for i in range(1,len(righe)):
    print(righe[i].split(",")[0])

nome="Alessio"
cognome="Manfredi"
via="sconosicuta"
stringa="\n"+nome+","+cognome+","+via
scrittura_file("1209/testCsv.txt",stringa)

contenuto =lettura_file("1209/testCsv.txt")

righe = contenuto.split("\n")

print(righe)

for i in range(1,len(righe)):
    print(righe[i].split(",")[0])
#C:\Users\Utilizzatore\Desktop\Academy\1209\testCsv.txt