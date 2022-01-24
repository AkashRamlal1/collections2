import string
import random

letters = list(string.ascii_letters)
nummers = list(string.digits)
Speciale_Tekens = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def space():
    print('')
    print('')


def generate_rando():

    space()

    lengte = int(input('hoeveel tekens moeten er in je wachtwoord'))

    lettter_teller = int(input('hoeveeel letters wil je in je wachtwoord'))

    nummer_teller = int(input('hoeveel nummers moeten in je wachtwoord'))

    speciale_tekens_teller = int(input('hoeveel spciale tekeens wil je in je wachtwoord'))

    TekenTeller = lettter_teller + nummer_teller + speciale_tekens_teller

    if TekenTeller > lengte:
        print("het aantal tekens is meer dan aangegeven aantal")
        return
    
    password = []
        
    for i in range(lettter_teller):
        password.append(random.choice(letters))

    for i in range(nummer_teller):
        password.append(random.choice(nummers))

    for i in range(speciale_tekens_teller):
        password.append(random.choice(Speciale_Tekens))

    if TekenTeller < lengte:
        random.shuffle(characters)
        for i in range(lengte - TekenTeller):
            password.append(random.choice(characters))
    
    random.shuffle(password)
    space()
    print('dit is je nieuwe wachtwoord:')
    space()

    print("".join(password))

generate_rando()

        
