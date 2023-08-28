""" Class utilized by solver algorithm containing methods of calculations for the value/weight of a word and current sum entropy which assists
in the word recommendation process utilized by the solver"""
#import statements
from decimal import Decimal, getcontext
import math 
import numpy as np

class Solver:

    def __init__(self, letterWeights):
        self.letterWeights = letterWeights

    def WordValueCalc(self, curTotalList, curPossList, dictLWFreq, DL04):
        """Calculate the value of a word out of the remaining guessable words based on information gained
        via previous guesses"""

        #Initialize variables
        getcontext().prec = 30
        wordValues = {}
        wordShortValues = {}
        totalSum = 0
        ShortSum = 0

        #Calculate weight of a word through the summation of its individual letters' probabilities
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

        """Implement the  only  rec poss words if <= 2 here probably"""

        #Get current sum of probabilities to normalize them
        Sum = sum(wordValues.values())
        ShortTotalSum = sum(wordShortValues.values())

        #Normalize probabilities. Therefore summation = 1 and everything is scaled
        for word in curTotalList:
            wordValues[word] = wordValues[word] / (Sum)
            if word in curPossList:
                wordShortValues[word] = wordShortValues[word] / (ShortTotalSum)

        #Calculate current total entropy for the remaining possible solution words
        totalEntropy = round(-np.sum(np.float64(float(value)) * np.log2(float(value)) for value in wordShortValues.values()), 5)
        if totalEntropy == -0.0:
            totalEntropy = 0.0

        #Return dictionary that has all the remaining guesable words and their weighted values
        return wordValues , totalEntropy