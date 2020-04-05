import random
class Player(object):
    def __init__(self, num, func):
        self.number = num
        self.choice = 'None'
        self.resultNum = -9999
        self.func = func
        self.active = True

    def show(self):
        print("player num:", self.number, "choice:", self.choice, "ourNum:", self.resultNum)

iterationCounter = 0
T = 4

def f1(X1,X2,T):
    if (X1>130):
        choice = 'S'
    else:
        choice = 'R'
    return choice

def f2(X1,X2,T):
    if (X2>100):
        choice = 'S'
    else:
        choice = 'R'
    return choice

def f3(X1,X2,T):
    if (T>2):
        choice = 'S'
    else:
        choice = 'R'
    return choice

def f4(X1,X2,T):
    if (X2-45 <= 30):
        choice = 'S'
    else:
        choice = 'R'
    return choice


Players = [Player(1, f1), Player(2, f2), Player(3, f3), Player(4, f4)]
print ([player.active for player in Players])

X1 = random.randint(0, 150)
# TODO where to put X2
X2 = random.randint(0, 150)



def calcResult(choice):
    if choice == 'S':
        ourNum = X1
    else:
        ourNum = random.randint(X2-45, X2+45)
    return ourNum


for player in Players:
    print(player.resultNum)



for player in Players:
    print(player.resultNum)



#while (iterationCounter < 100):
while (T > 0):
    ourNum = 0

    print("new round----------------------------------------------------")
    print("number of active players:", len(Players))

    X1 = random.randint(0, 150)
    #TODO move somewhere
    X2 = random.randint(0, 150)

    #for every player activate the descision function
    for player in Players:
        player.choice = player.func(X1, X2, T)

    for player in Players:
        player.resultNum = calcResult(player.choice)

    for player in Players:
        print(player.resultNum)

    resultNums = (player.resultNum for player in Players)
    print("min num : ")
    minNum = min(resultNums)
    print(minNum)

    # array of results

    Players = list(filter(lambda player: player.resultNum > minNum, Players))

    #how to eliminate only 1 player each turn


    # for player in Players:
    #    print(player.resultNum)
    #remove someone from Players
    T=T-1











