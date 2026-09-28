luku = input("Anna luku tai paina Enter lopettaaksesi:")
pienin = None
suurin = None
while luku != "":
    numero = float(luku)

    if pienin == None:
        pienin = numero
        suurin = numero
    else:
        if numero < pienin :
            pienin = numero
        if numero > suurin :
            suurin = numero
    
    luku = input("Anna luku tai paina Enter lopettaaksesi:")
print("Pienin luku on", pienin)
print("Suurin luku on", suurin)
    

