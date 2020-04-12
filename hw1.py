import random
import numpy as np


class Player(object):
    def __init__(self, num, func):
        self.number = num
        self.choice = 'None'
        self.resultNum = -9999
        self.func = func
        self.eliminatedOnRound = -1
        self.active = True

    def show(self):
        print("player num:", self.number, "choice:", self.choice, "ourNum:", self.resultNum)


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


iterations = 1000
iterationCounter = 0
T = 4
Players = [Player(1, f1), Player(2, f2), Player(3, f3), Player(4, f4)]
ActivePlayers = Players
resultsVector = [0, 0, 0, 0]
print([player.active for player in ActivePlayers])


def calcResult(choice):
    if choice == 'S':
        ourNum = X1
    else:
        #ourNum = random.randint(X2-45, X2+45)
        ourNum = np.random.normal(X2, 45, 1)  # sample from Normal distribution
    return ourNum


def eliminatePlayer(min_result):
    new_players = list(filter(lambda player: player.resultNum == min_result, ActivePlayers))
    """
    print("min players : ")
    for player in new_players:
        print(player.resultNum)
    """

    player_to_eliminate = random.randint(0, len(new_players) - 1)
    #print("player_to_eliminate from all minimum results array : ", player_to_eliminate)
    #print("eliminating result : ", new_players[player_to_eliminate].resultNum)
    num_to_eliminate = new_players[player_to_eliminate].number
    #print("num_to_eliminate : ", num_to_eliminate)
    return num_to_eliminate


def printNewRoundData(min_result):
    print("new round----------------------------------------------------")
    print("number of active players:", len(ActivePlayers))
    print("player results:")
    for player in ActivePlayers:
        print(player.resultNum)

    print("min num : ", min_result)


def setupPlayersForNewIteration():
    for player in Players:
        player.active = True
        player.eliminatedOnRound = -1


while (iterationCounter < iterations):
    print("iteration ", iterationCounter)
    X1 = random.randint(0, 150)

    setupPlayersForNewIteration()
    ActivePlayers = Players
    T = 4

    while (T > 0):

        #  for every player activate the descision function
        for player in ActivePlayers:
            X2 = random.randint(0, 150)
            player.choice = player.func(X1, X2, T)

        for player in ActivePlayers:
            player.resultNum = calcResult(player.choice)

        resultNums = (player.resultNum for player in ActivePlayers)

        minNum = min(resultNums)
        # printNewRoundData(minNum)

        # if there are at least 2 active players
        if len(ActivePlayers) > 1:
            num_to_eliminate = eliminatePlayer(minNum)
            for player in Players:
                if player.number == num_to_eliminate:
                    player.active = False
                    player.eliminatedOnRound = T
                    break
            ActivePlayers = list(filter(lambda player: player.number != num_to_eliminate, ActivePlayers))

        T -= 1

    for player in Players:
        print("player num: ", player.number, " eliminated on round: ", player.eliminatedOnRound)
        if player.eliminatedOnRound == -1:
            resultsVector[player.number - 1] += 1

    iterationCounter += 1

print("printing overall results of winners")
print (resultsVector)









