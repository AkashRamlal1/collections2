boodschappenlijst = []


kopen = True

while kopen == True:
    
    toevoegen = input('wat wil je kopen?')
    boodschappenlijst.append(toevoegen)

    aantal = int(input('hoeveel wil je ervan'))
    
    print("op je lijstje staat")
    print("-----")
    for item in boodschappenlijst:
        print("-  " + int(aantal), item)
    print("-----")

    antwoord = input("wil je meer toevoegen?  (J/N)")
    if antwoord == "N" or antwoord == "n":
        kopen = False

    if aantal in boodschappenlijst:
        boodschappenlijst[toevoegen] += aantal
    
    print("dit wil je kopen:  ")
    print("-----")
    for item in boodschappenlijst:
        print("-  " + int(aantal), item)
    print("-----")
