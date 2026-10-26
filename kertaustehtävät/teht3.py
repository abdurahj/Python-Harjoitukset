while True :
    print("Tuote valmistettu!")
    vastaus = input("Jatketaanko tuontantoa? (vastaa EI jos haluat lopettaa ohjelman :)").capitalize()
    if vastaus == ("Ei") :
        break
print("Tuotanto lopetettu!")
