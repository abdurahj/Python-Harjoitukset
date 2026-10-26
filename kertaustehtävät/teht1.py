tuntipalkka = float(input("Kuinka paljon on sinun tuntipalkkasi :"))
tunnit = float(input("Kuinka monta tuntia teit töitä :"))
päivä = input("Mikä viikkonpäivä :")
päiväpalkka = tuntipalkka * tunnit
if päivä == "sunnuntai":
    päiväpalkka = 2*(tuntipalkka * tunnit)
print(f"Päiväpalkkasi on {päiväpalkka} euroa")
