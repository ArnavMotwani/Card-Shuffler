import random as r

def generateShuffledPack():
    suites = ["C", "S", "H", "D"] # Generating Suites
    cards = ["A", "J", "Q", "K"]+["0"+str(_) if _ < 10 else str(_) for _ in range(2, 11)] # Generating cards per suite
    pack = [card+" - "+suite for card in cards for suite in suites] # Generating unshuffled pack
    for card in r.sample(pack, 52): # shuffling pack and displaying it
        print(card)

generateShuffledPack()