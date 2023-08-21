#parameters = current list, 5 specific spot lists w their respective probabilities before or after 
#letters were eliminated, dictionary of probabilities for letters in specific spots
#weights of words (probabilities of each letter combined)

#probability of a letter in a specific spot list = probability of that letter out of  the current
#letters available in that spot * probability of that letter in that specific spot to determine weight
from decimal import Decimal, getcontext
import operator
import math 
#calculate value of a word
class Solver:

    def __init__(self, letterWeights):
        self.letterWeights = letterWeights

    #calculate the "value" of each word out of the remaining words 
    #based on the current information
    def WordValueCalc(self, curTotalList, curPossList, dictLWFreq, DL04):
        getcontext().prec = 30
        wordValues = {}
        wordShortValues = {}
        totalSum = 0
        ShortSum = 0
        for word in curTotalList:
            wordValues[word] = 0
            checkDuplicates = []
            if word in curPossList:
                wordShortValues[word] = 0
                checkShortDuplicates = []
            for i in range(len(word)):
                if word[i] not in checkDuplicates:
                    checkDuplicates.append(word[i])
                    totalSum += (Decimal(DL04[i][word[i].upper()])
                                 * (Decimal(self.letterWeights[word[i].upper()])))
                if word in curPossList and word[i] not in checkShortDuplicates:
                    checkShortDuplicates.append(word[i])
                    ShortSum += (Decimal(DL04[i][word[i].upper()])
                                 * (Decimal(self.letterWeights[word[i].upper()])))
            wordValues[word] = totalSum
            totalSum = 0
            if word in curPossList:
                wordShortValues[word] = ShortSum
                ShortSum = 0

        Sum = sum(wordValues.values())
        ShortTotalSum = sum(wordShortValues.values())
        for word in curTotalList:
            wordValues[word] = wordValues[word] / (Sum)
            if word in curPossList:
                wordShortValues[word] = wordShortValues[word] / (ShortTotalSum)

        #calculate current total entropy for the remaining possible solution words
        totalEntropy = round(-sum(float(str(value)) * math.log2(value) for value in wordShortValues.values()), 5)
        if totalEntropy == -0.0:
            totalEntropy = 0.0

        #return dictionary that has all the remaining guesable words and their weighted values
        return wordValues , totalEntropy