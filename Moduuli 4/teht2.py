tuumat=float(input("Anna tuumamäärä"))
muunnos = 2.54
while tuumat >= 0:
    sentit = tuumat * muunnos
    print(f"{tuumat}tuumaa on {sentit} cm")
    tuumat =float(input("Anna tuumamäärä: "))
    