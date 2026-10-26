tarina = " "
edellinen = " "
while True:
    sana = input("Anna sana tarinaana(kirjoita loppu lopettaaksesi)")
    if sana == "loppu":
        break
    if sana == edellinen :
        break
    tarina = tarina + sana + " "
    edellinen = sana
print(tarina)

