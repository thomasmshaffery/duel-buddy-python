from duelist import Duelist
from dos import matrix
from dos_ranks import Ranks

class Duel():
    def __init__(self):
        self.duelist1 = Duelist()
        self.duelist2 = Duelist()
        self.isTitle = False
        self.currentRound = 1
        self.ring = "Default"
        self.sport = "dos"
        self.matrix = matrix

    def setRingName(self, name):
        self.ring = name
        
    def getRound(self):
        return self.currentRound

    def printRound(self):
        print("Round:" + self.getRound() )

    def handleMove(self, move1, move2):
        return self.matrix[move1][move2]

    def gameLoop(self):
        
        self.setRingName(input("Ring Name: "))
        self.duelist1.setName(input("Name Duelist 1: "))
        self.duelist1.setRank(Ranks.COMMONER)
        self.duelist2.setName(input("Name Duelist 2: "))
        self.duelist2.setRank(Ranks.COMMONER)

        while self.currentRound < 16:
            duelist1Move = input("Select duelist 1's move: ").lower()
            duelist2Move = input("Select duelist 2's move: ").lower()

            self.duelist1.updateScore(self.handleMove(duelist1Move, duelist2Move))
            self.duelist2.updateScore(self.handleMove(duelist2Move, duelist1Move))

            print("{ring} {0}: {1} used {2} and {3} used {4} - {5} - {6}".format(self.currentRound, self.duelist1.getName(), duelist1Move, self.duelist2.getName(), duelist2Move, self.duelist1.getScore(), self.duelist2.getScore(), ring=self.ring))
            self.currentRound += 1
