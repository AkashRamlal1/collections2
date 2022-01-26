from posixpath import split
import random
def deck(): #maakt de stapel kaarten
    stapel = []
    kleur = ['Rood','Blauw','Geel','groen']
    regulier = ['0','1','2','3','4','5','6','7','8','9','skip','reverse','draw +2']
    special = ['wild','draw +4']
    for colour in kleur:
        for value in regulier:
            kaartwaarde = "{} {}".format(colour,value)
            stapel.append(kaartwaarde)
            if regulier != 0:
                stapel.append(kaartwaarde)
    for i in range(4):
        stapel.append(special[0])
        stapel.append(special[1])

    random.shuffle(stapel)
    random.shuffle(stapel)
    

    return stapel


#met deze functie trek je kaarten van de stapel

def drawCards(numcards):
    cardsDrawn = []
    for i in range(numcards):
        cardsDrawn.append(UNO_Deck.pop(0))
    return cardsDrawn

def showHand(player,playerhand):
    print("")
    print("speler {}'s beurt".format(player+1))
    print("dit is je hand")
    print("--------------------")
    y = 1
    for card in playerhand:
        print("{}) {}".format(y,card))
        y+=1
    print("")

    if playerhand == 0:
        print("UNO")
        

def CanPlay(colour,value,playerhand):
    for card in playerhand:
        if "wild" in card:
            return True
        elif colour in card or value in card:
            return True
    return False


        
UNO_Deck = deck()
discards = []
print(UNO_Deck)

spelers = []
kleurtje = ['Rood','Blauw','Geel','groen']
numspelers = int(input('hoeveel spelers zijn er'))
while numspelers<2 or numspelers>4:
    numspelers = int(input('dat is niet mogelijk voer een ander aantal in'))
for player in range(numspelers):
    spelers.append(drawCards(7))


print(spelers)

SpelerBeurt = 0
playerdiirection = 1
playing = True
discards.append(UNO_Deck.pop(0))
splitCard = discards[0].split(" ", 1)
currentcolour = splitCard[0]
if currentcolour != "wild":
    cardVal = splitCard[1]
else:
    cardval = "any"




while playing:
    showHand(SpelerBeurt,spelers[SpelerBeurt])
    print("bovenste kaart is: {}".format(discards[-1]))
    if CanPlay(currentcolour , cardVal , spelers[SpelerBeurt]):
        gekozenKaart = int(input('welke kaart wil je gebruiken'))
        while not CanPlay(currentcolour,cardVal,[spelers[SpelerBeurt][gekozenKaart-1]]):
            gekozenKaart = int(input("deze kaart kan je niet spelen kies een ander"))
        print("je hebt {} gebruikt".format(spelers[SpelerBeurt][gekozenKaart-1]))
        discards.append(spelers[SpelerBeurt].pop(gekozenKaart-1))
        if len(splitCard) == 1:
                cardVal = "Any"
        else:
            cardVal = splitCard[1]
        if currentcolour == "wilds" :
            for x in range (len(kleurtje)):
                print("{} ) {}".format(x+1 , kleurtje[x]))
            nieuwekleur = int(input('welke kleur wil je'))
            while nieuwekleur < 1 or nieuwekleur > 4:
                nieuwekleur = int(input('niet mogelijk. welke kleur will je kiezen voer het nuummer in'))
            currnetColour = kleurtje[nieuwekleur-1]
        if cardVal == "reverse":
            playerdiirection = playerdiirection * -1
        elif cardVal == "skip":
            SpelerBeurt += playerdiirection
        if SpelerBeurt >= numspelers:
            SpelerBeurt = 0
        elif SpelerBeurt < 0:
            SpelerBeurt = spelers[numspelers-1]
        elif cardVal ==  "draw two":
            pak_kaart =  SpelerBeurt+playerdiirection
            if SpelerBeurt == numspelers:
                SpelerBeurt = 0
            elif SpelerBeurt <0:
                SpelerBeurt = numspelers-1
                spelers[SpelerBeurt].extend(drawCards(2))
        elif cardVal == "draw four":
            pak_kaart =  SpelerBeurt+playerdiirection
            if SpelerBeurt == numspelers:
                SpelerBeurt = 0
            elif SpelerBeurt < 0:
                SpelerBeurt = numspelers-1
                spelers[SpelerBeurt].extend(drawCards(2))


    #checkt oest kaarten
    speelkaartsplt = discards[-1].split(" ",1)
    currentcolour = splitCard[0]
    if len(splitCard) == 1:
        cardval = "any"
    else:
        cardval = splitCard[1]
    




    SpelerBeurt += playerdiirection
    if SpelerBeurt == numspelers:
        SpelerBeurt = 0
    elif SpelerBeurt < 0:
        SpelerBeurt = numspelers -1
        
    
    
