import random 
doorgaan = True
while doorgaan:
    dobbelsteen = ['0','0','0','0','0']

    #de values van mde dobbelsttenen zijn in het begin allemaal 0
    for i in range(5):
        dobbelsteen[i] = random.randint(1,6)

    #hier worden eigen waardes gegeven aan de dobbelstenen 
    print("je nummers zijn:", dobbelsteen)
    dobbelsteen.sort()
    if dobbelsteen[0] == dobbelsteen[4]:
        print('YAHTZEE!')
    elif (dobbelsteen[0] == dobbelsteen[3]) or (dobbelsteen[1] == dobbelsteen[4]):
        print('Four of a kind')
    elif ((dobbelsteen[0] == dobbelsteen[2]) or (dobbelsteen[1] == dobbelsteen[3]) or (dobbelsteen[2] == dobbelsteen[4])):
        print("three of a kind")
    doorgaan = (input("klik op [Enter] om door te gaan, klik op een andere toets om tee stoppen:") == "")
    # het spel blijft doorgaan als je op entter drukt omdatt doorgaan true is zodra je een andere toets kiest verranderd doorgaan naar false