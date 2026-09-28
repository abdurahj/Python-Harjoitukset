oikea_tunnus = "python"
oikea_salasana = "kante8"
tunnus =input("Anna käyttjätunnnus: ")
salasana =input("Anna salasana: ")
yritykset = 0

while yritykset < 5:
    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else :
        yritykset += 1
        tunnus = input("Anna käyttäjätunnus uudestaa: ")
        salasana = input("Anna salasana uudestaan: ")
if yritykset >= 5:
    print("Pääsy evätty")
