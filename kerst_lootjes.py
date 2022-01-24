import random

stop  = False
spelers = []

while stop == False:

    toevoegen = input('voeg een naam toe of typ stop')
    if toevoegen in spelers:
        print('deze naam staat er al kies een andere')
        toevoegen = input('voeg een naam toe of typ stop')
    spelers.append(toevoegen)
    for item in spelers:
        print("-  " + item )
        print('')

    if toevoegen == 'stop':
        spelers.remove('stop')
        random.shuffle(spelers)
        for i in range(len(spelers)):
            
            
            
            print(spelers[i],"buys for",spelers[(i+1)%(len(spelers))])
            

        stop = True



