lentoasemat = {}
while True:
    valinta = input("1 = Lentoasema, 2 = Hae lentoasema, 3 = Lopeta: ")
    if valinta == "3" :
        break
    elif valinta == "1" :
        koodi = input ("Anna lentoaseman ICAO-koodi: ")
        nimi = input ("Anna lentoaseman nimi: ")
        lentoasemat[koodi] = nimi
    elif valinta == "2":
       koodi = input ("Anna lentoaseman ICAO-koodi: ")
       if koodi in lentoasemat :
           print (lentoasemat[koodi])
       else :
           print ("Lentoasema ei löytynyt")

