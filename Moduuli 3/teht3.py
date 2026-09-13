sukupuoli = input("Anna biologinen sukupuoli (nainen/mies):")
hemoglobiini = int(input("Anna hemoglobiiniarvo (g/l):"))
if sukupuoli == "nainen" :
    if hemoglobiini < 117 :
        print("alhainen arvo")
    elif hemoglobiini > 175 :
        print("korkea arvo")
    else :
        print("normaali arvo")
elif sukupuoli == "mies":
    if hemoglobiini < 134 :
        print("alhainen arvo")
    elif hemoglobiini > 195 :
        print("korkea arvo")
    else :
        print("normaali arvo")
else :
    print("virheellinen sukupuoli")