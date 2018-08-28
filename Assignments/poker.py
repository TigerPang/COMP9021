from random import randint,seed
import sys

seed(0)

cardsNum=[0, 0, 0, 0, 0, 0]
cards=["Ace", "King", "Queen", "Jack", "10", "9"]

prability = [0, 0, 0, 0, 0, 0, 0]

def check(card):
    if card == "Ace":
        return 0
    if card == "King":
        return 1
    if card == "Queen":
        return 2
    if card == "Jack":
        return 3
    if card == "10":
        return 4
    if card == "9":
        return 5
    return -1
    
def next():
    global cardsNum
    keepNum=[0, 0, 0, 0, 0, 0]
    keep = []

    while True:
        try:
            keep = input("Which dice do you want to keep for the second roll?").split()
            if len(keep) == 1 and (keep[0] == "all" or keep[0] == "All"):
                print("OK, done.")
                sys.exit()
            for card in keep:
                num = check(card)
                #print(num)
                if num == -1:
                    raise ValueError
                keepNum[num] = keepNum[num] + 1
            for i in range(6):
                if keepNum[i] > cardsNum[i]:
                    raise ValueError
            break
        except ValueError:
            print("That is not possible, try again!")

    if len(keep) == 5:
        print("OK, done.")
        sys.exit()

    for i in range(6):
        cardsNum[i] = keepNum[i]
  
    getNewCard( 5 - len(keep) )
    
    print( "It is a " + checkHand() )
    next()

def checkHand():
    global prability
    max1, max2 = 0, 0 
    for i in range(6):
        if cardsNum[i] > max1:
            max1 = cardsNum[i]
            max2 = 0
        elif cardsNum[i] == max1:
            max2 = max1

    if max1 == 5:
        prability[0] = prability[0] + 1
        return "Five of a kind"
    if max1 == 4:
        prability[1] = prability[1] + 1
        return "Four of a kind"
    if max1 == 3 and max2 == 2:
        prability[2] = prability[2] + 1
        return "Full house"
    if max1 == 3:
        prability[4] = prability[4] + 1
        return "Three of a kind"
    if max1 == 2 and max2 == 2:
        prability[5] = prability[5] + 1
        return "Two pair"
    if max1 == 2:
        prability[6] = prability[6] + 1
        return "One pair"
    if cardsNum[0] == 0 or cardsNum[5] == 0:
        prability[3] = prability[3] + 1
        return "Straight"

    return "Bust"

def getNewCard(n):
    global cardsNum
    for i in range(n):
        x = randint(0, 5) 
        #print(x)
        cardsNum[x] = cardsNum[x] + 1
    res = "The roll is"
    for i in range(6):
        for j in range(cardsNum[i]):
            res = res + " " + cards[i]
    print(res)


def play():
    getNewCard(5)
    print( "It is a " + checkHand() )
    next()

def simulate(times):
    global prability
    prability = [0, 0, 0, 0, 0, 0, 0]
    for i in range(times):
        cardsNum = [0, 0, 0, 0, 0, 0]
        getNewCard(5)
        checkHand()

    print("Five of a kind : " + "{:.2%}".format(prability[0] / times) )
    print("Four of a kind : " + "{:.2%}".format(prability[1] / times) )
    print("Full house : " + "{:.2%}".format(prability[2] / times) )
    print("Straight : " + "{:.2%}".format(prability[3] / times) )
    print("Three of a kind : " + "{:.2%}".format(prability[4] / times) )
    print("Two pair : " + "{:.2%}".format(prability[5] / times) )
    print("One pair : " + "{:.2%}".format(prability[6] / times) )
    
        
play()        
simulate(10)

