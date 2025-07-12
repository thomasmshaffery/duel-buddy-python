from duelist import Duelist
from dos import matrix

class Duel():
    def __init__(self):
        self.duelist1 = Duelist()
        self.duelist1.name = "Dummy"
        self.duelist2 = Duelist()
        self.currentRound = 4
        self.ring = "Default"
        self.sport = "dos"
        self.matrix = matrix

    def setRingName(self, name):
        self.ring = name
        
    def getRound(self):
        return self.currentRound

    def printRound(self):
        print("Round:" + self.getRound() )

