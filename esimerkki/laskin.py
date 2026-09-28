print("----------TERVETULOAS lASKINOHJELMAAN--------")

print("Valitse mitä toimintoa haluat käyttä")
print("A: Yhteenlaskua, B: Vähennyslasku, C: Kertolasku, D: Jakolasku")
valinta = input("Anna valintaasi")

a = float(input("Anna ensimäinen luku"))
b = float(input("Anna toinen luku"))

    while True:
        if valinta == "A":
        print(f"Lukujen {a} ja {b} summa on {a+b}")
            elif valinta == "B":
         print(f"Lukujen {a} ja {b} erotus on {a-b}")
     
        elif valinta == "C":
        print(f"Lukujen {a} ja {b} tulo on {a*b}")
   
        elif valinta == "D":
         print(f"Lukujen {a} ja {b} osamäärä on {a/b}")
    e   lse:
        print("Virheellinen valinta")
     
     
