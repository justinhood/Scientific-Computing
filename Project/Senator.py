import numpy as np
class Senator:
    def __init__(self, name, n, party):
        self.name=name
        self.votes=np.zeros(n)
        self.party=party
    
    def printName(self):
        print(self.name)
    def getName(self):
        return self.name
    def getVotes(self):
        return self.votes
    def getParty(self):
        return self.party
    def printVotes(self):
        print(self.votes)
    def setVotes(self, val, pos):
        self.votes[pos]=val
