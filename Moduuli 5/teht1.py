import random
luku = int(input("Kuinka monta arpakuutioita heitetään?"))
summa = 0
for i in range(luku):
    heitto = random.randint(1,6)
    summa = summa + heitto
print(f"Yhteisumma on {summa}")