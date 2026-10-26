import math 
while True :
    luku =int(input("Anna kokonaisluku :"))
    if luku == 0 :
        break
    elif luku < 0:
        print("virheellinen numero")
    else :
        print (math.sqrt(luku))
