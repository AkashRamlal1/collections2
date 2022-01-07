boodschappenlijst = []

kopen = True

while kopen == True:
    
    toevoegen = input('wat wil je kopen?')
    boodschappenlijst.append(toevoegen)
    print("op je lijstje staat")
    print("-----")
    for item in boodschappenlijst:
        print("-  " + item)
    print("-----")

    antwoord = input("wil je meer toevoegen?  (J/N)")
    if antwoord == "N" or antwoord == "n":
        kopen = False
    
    print("dit wil je kopen:  ")
    print("-----")
    for item in boodschappenlijst:
        print("-  " + item)
    print("-----")
