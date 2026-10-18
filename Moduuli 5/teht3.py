luku = int(input("Anna kokonaisluku: "))
jaollinen = False
for jakaja in range(2, luku):           #jos annat luvuksi 9, se kokeilee luvut 2-8 yksi kerrallaan
    if luku % jakaja == 0:              # jakaja luku jolla kokeillaan jakamista. Vaihtuu joka kierroksilla
        jaollinen = True                # Jos jakojäännös on 0, jako menee tasan ja merkitään jaollinen = True
if luku < 2:                            # onko luku pienempi kuin 2, jos ei jatketaan
    print("Luku ei ole alkuluku")       
elif jaollinen:                             
    print("Luku ei ole alkuluku")
else :
    print("Luku on alkuluku")