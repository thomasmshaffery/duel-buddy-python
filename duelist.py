from dos_ranks import Ranks

class Duelist():
    def __init__(self):
        self.name = ""
        self.rank = None
        self.mods = 0
        self.score = 0
        self.mage_spell = ""

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setRank(self, rank):
        self.rank = rank

    def setMods(self):
        def __allocateMods(rank):
            match rank:
                case Ranks.COMMONER:
                    self.mods = 0
                case Ranks.SWORDSMAN:
                    self.mods = 1
                case Ranks.MASTER_AT_ARMS:
                    self.mods = 2
                case Ranks.GRANDMASTER:
                    self.mods = 3
                case Ranks.WARLORD:
                    self.mods = 4
                case Ranks.BARON:
                    self.mods = 5
                case Ranks.OVERLORD:
                    self.mods = 6

        __allocateMods(self.rank)
        
    def getMods(self):
        return self.mods

    def updateScore(self, result):
        self.score += result
    
    def getScore(self):
        return self.score
    

        
        
