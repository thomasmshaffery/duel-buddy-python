class Duelist():
    def __init__(self):
        self.name = ""
        self.rank = ""
        self.mods = 0
        self.score = 0
        self.mage_spell = ""

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMods(self, mods):
        self.mods = mods
        
    def getMods(self):
        return self.mods

    def scorePoint(self):
        self.score += 1
    
    def getScore(self):
        return self.score

        
        
