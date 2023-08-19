#parameters = current list, 5 specific spot lists w their respective probabilities before or after 
#letters were eliminated, dictionary of probabilities for letters in specific spots
#weights of words (probabilities of each letter combined)

#probability of a letter in a specific spot list = probability of that letter out of  the current
#letters available in that spot * probability of that letter in that specific spot to determine weight
from decimal import Decimal, getcontext
#calculate value of a word
class Solver:
    #DL1 = Dictionary for possible letters and their probabilities in spot 1
    def __init__(self, letterWeights):
        self.letterWeights = letterWeights

    #calculate the "value" of each word out of the remaining words 
    #based on the current information
    def WordValueCalc(self, curTotalList, curPossList, dictLWFreq, DL04):
        getcontext().prec = 30
        wordValues = {}
        print(DL04)
        for word in curTotalList:
            if word in curPossList:
                curWord = word + "***"
                wordValues[word + "***"] = 0
            else:
                curWord = word
                wordValues[word] = 0
            checkDuplicates = []
            for i in range(len(word)):
                if word[i] not in checkDuplicates:
                    checkDuplicates.append(word[i])
                    wordValues[curWord] += Decimal(DL04[i][word[i].upper()]) 
                                            #* Decimal(self.letterWeights[word[i].upper()]))
            #(Decimal(dictLWFreq[word[i].upper()][i]) *
            wordValues[curWord] = float(str(round(wordValues[curWord], 4)))

        for word in curTotalList:
            if word in curPossList:
                curWord = word + "***"
            else:
                curWord = word
            wordValues[curWord] = wordValues[curWord] / (sum(wordValues.values()))

        sortedWordValues = dict(sorted(wordValues.items(), key = lambda x: x[1], reverse = True))

        #return dictionary that has all the words and their values sorted from largest to smallest
        return sortedWordValues