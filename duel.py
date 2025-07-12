from duelist import Duelist
from dos_ranks import Ranks

class Duel():
    def __init__(self):
        duelist1 = None
        duelist2 = None
        round = 0
        ring = ""
        sport = ""
        matrix = []

        def setDuelist1(Duelist):
            self.duelist1 = Duelist
        
        def setDuelist2(Duelist):
            self.duelist2 = Duelist

