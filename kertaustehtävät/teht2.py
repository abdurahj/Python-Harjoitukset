luku = int(input("Anna joku kokonaisluku, jonka jälkeen ohjelma kertoo onko jaollinen 3:lla , 5:llä vai molemmilla :"))
if luku % 3 == 0 and luku % 5 == 0 :
    print("jaollinen molemilla")
elif luku % 3 == 0 :
    print("luku on jaollinen kolmella")
elif luku % 5 == 0 :
    print("luku on jaolllinen viidellä")
else :
    print ("ei jaollinen kummallakaan")