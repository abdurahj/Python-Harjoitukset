luvut = []
annettu_luku =input("Anna luku tai lopeta Painamalla ENTER:")
while annettu_luku != "":
    luku = float(annettu_luku)
    luvut.append(luku)
    annettu_luku =input("Anna luku tai lopeta Painamalla ENTER:")
luvut.sort(reverse=True)        #sort = järjestää listan ja reverse=True = suurimmasta pienimpään
for luku in luvut[:5]:          # [:5] valitsee 5 ensimmäistä 
    print(luku)