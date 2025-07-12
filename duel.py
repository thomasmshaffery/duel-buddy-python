from duelist import Duelist
from dos_ranks import Ranks

class Duel():
    def __init__(self):
        self.duelist1 = Duelist()
        self.duelist1.name = "Dummy"
        self.duelist2 = Duelist()
        self.currentRound = 4
        self.ring = "Test"
        self.sport = "dos"
        self.matrix = []

        def setDuelist1(Duelist):
            self.duelist1 = Duelist()
        
        def setDuelist2(Duelist):
            self.duelist2 = Duelist()
        
        def printDuelists(self):
            print(duelists)
        
        def getRound(self):
            return currentRound

    def printRound(self):
        print("Round:" + self.getRound() )

