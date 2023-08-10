#parameters = current list, 5 specific spot lists w their respective probabilities before or after 
#letters were eliminated, dictionary of probabilities for letters in specific spots
#weights of words (probabilities of each letter combined)

#probability of a letter in a specific spot list = probability of that letter out of  the current
#letters available in that spot * probability of that letter in that specific spot to determine weight

class AlgorithmCalc:
    #DL1 = Dictionary for possible letters and their probabilities in spot 1
    def __init__(self, curTotalList, DL0, DL1, DL2, DL3, DL4, WordWeights):
        self.curTotalList = curTotalList
        self.DL0 = DL0
        self.DL1 = DL1
        self.DL2 = DL2
        self.DL3 = DL3
        self.DL4 = DL4
        self.wordWeights = WordWeights

    def AlgCalc(self):
        pass