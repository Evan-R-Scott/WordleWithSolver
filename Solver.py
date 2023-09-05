"""              Modularized Code for Solver             """
#import statements
import DatasetDictionaryInitialization
from AlgorithmCalc import SolverCalculations

import tkinter as tk
import heapq
from decimal import Decimal, getcontext

class WordleSolver:

    def __init__(self, solver_frame):
        self.solver_frame = solver_frame
    
    def variablesInitialization(self):
        
        getcontext().prec = 30

        #Initialize the list containing 5 dictionaries for each specific spot with letters and probabilities
        #that get removed and renormalised based on a guess making letters green/gray/yellow
        self.totalLettersdictLWFreq = DatasetDictionaryInitialization.totalLettersdictLWFreq
        self.dictLWFreq = DatasetDictionaryInitialization.dictLWFreq
        
        #Files to be opened and read
        self.LONG_WORDLIST_FILENAME = "/Users/evanp/OneDrive/Desktop/Individual Projects/WordleRepo/long_wordlist.txt"
        self.SHORT_WORDLIST_FILENAME = "/Users/evanp/OneDrive/Desktop/Individual Projects/WordleRepo/short_wordlist.txt"

        self.curTotalwrds = []
        f = open( self.LONG_WORDLIST_FILENAME, 'r')
        for wrd in f:
            self.curTotalwrds.append(wrd.strip())
        f.close()

        self.curPosswrds = []
        f = open(self.SHORT_WORDLIST_FILENAME, 'r')
        for wrd in f:
            self.curPosswrds.append(wrd.strip())
        f.close()

        self.DL04 =  []
        for i in range(5):
            new_dict = {key: value for key, value in self.totalLettersdictLWFreq.items()}
            self.DL04.append(new_dict)
            for key in self.DL04[i]:
                self.DL04[i][key] = (self.DL04[i][key] * (self.dictLWFreq[key][i]))
            totalSum =  sum(self.DL04[i].values())
            for key in self.DL04[i]:
                self.DL04[i][key] = float(str(Decimal(self.DL04[i][key]) / Decimal(totalSum)))

        #Solver variables
        self.FontHeader = 8
        self.KeyFont = 7
        self.FontRecommendations = 4
        self.FONT_FAMILY = 'ariel' 
        self.KeyText = (self.FONT_FAMILY, self.KeyFont)
        self.Header = (self.FONT_FAMILY, self.FontHeader)
        self.HeaderBig = (self.FONT_FAMILY, self.KeyFont, 'bold', 'underline')
        self.Title = "Solver"
        self.totalWordsRemaining = "Guessable Words Remaining:"
        self.currentEntropy = "Current Entropy/Uncertainty:"
        self.possibleOutcomeText = "Potential Solution Words Remaining:"
        self.RecommendationHeader = "Top Picks || Possible Solution || P(Word)"
        self.Key = "Key Info"
        self.Key1 = "- TOP PICKS : Of the remaining words, the words within this column are the top recommendations offered by the solver as they offer the most value towards completing the Wordle."
        self.Key2 = "- POSSIBLE SOLUTION: (Yes) indicates this recommended word is within the Wordle word list and therefore is a potential solution for the Wordle. Absence of a (Yes) suggests the word is from the list of accepted guessable words but cannot be the Wordle solution."
        self.Key3 = "- P(WORD) : Probability/Weight of a word's value within the set of remaining guessable words. A word's value is the summation of its letters' normalized probalities."

    def solver(self, ColorForLetterInfo, curGuess, gameStarted, solverBool):
        self.ColorForLetterInfo = ColorForLetterInfo
        self.curGuess = curGuess
        self.gamestarted = gameStarted
        self.solver_bool = solverBool
        
        self.variablesInitialization()
        #create instance of Solver Calculations class
        self.SolverCalc = SolverCalculations(self.totalLettersdictLWFreq)

        self.solverDictUpdate()
        self.solverDisplay()
        self.normalization()

    def solverDictUpdate(self):
        for i in range(len(self.curGuess)):
            #green letter handler
            if self.curGuess[i] in self.ColorForLetterInfo[2][i]:
            #keeps track of where correct letters are located when found so we can test other uncertain letters
                #in that already determined location's answer
                self.DL04[i] = {self.ColorForLetterInfo[2][i]: 1.0}
            #yellow letter handler
            elif (self.curGuess[i] not in  self.ColorForLetterInfo[1][i] and (len(self.DL04[i]) > 1)):
                self.DL04[i] = {key: self.DL04[i][key] for key in self.DL04[i]
                                if key != self.curGuess[i]}
            elif self.curGuess[i] in self.ColorForLetterInfo[0]:
            #Handle gray letter removal from dictionaries
                for dictionary in self.DL04:
                # if self.curGuess[i] in self.ColorForLetterInfo[0] and self.curGuess[i] in dictionary:
                #maybe put these lines after line 447 for gray letter elimination from self.dl04
                    if self.curGuess[i] in dictionary:
                        del dictionary[self.curGuess[i]]
    
    def normalization(self):
        """Updates lists for solver algorithm and normalization of probabilities based on 
            gray/yellow letters from previously guessed word"""
        getcontext().prec = 30
        curG = 0

        for dictionary in self.DL04:
            for i in range(len(self.curTotalwrds) - 1, -1, -1):
                if self.curTotalwrds[i][curG].upper() not in dictionary.keys():
                    del self.curTotalwrds[i]
            for i in range(len(self.curPosswrds) - 1, -1, -1):
                if self.curPosswrds[i][curG].upper() not in dictionary.keys():
                    del self.curPosswrds[i]
            totalSum =  sum(Decimal(value) for value in dictionary.values())
            if len(dictionary) > 1:
                for key in dictionary:
                    dictionary[key] = Decimal(dictionary[key])/ totalSum
            curG += 1

        if len(self.ColorForLetterInfo[3]) > 0:
            self.curTotalwrds = [word for word in self.curTotalwrds if all(letter.lower() in word for letter in self.ColorForLetterInfo[3])]
            self.curPosswrds = [word for word in self.curPosswrds if all(letter.lower() in word for letter in self.ColorForLetterInfo[3])]       

        self.TotalWordsCount = len(self.curTotalwrds)
        self.PossibleWordsCount = len(self.curPosswrds)
        self.wordsRem.set(self.totalWordsRemaining + "\n" + str(self.TotalWordsCount))
        self.possWordsRem.set(self.possibleOutcomeText + "\n" + str(self.PossibleWordsCount))
        self.curEntRem.set(self.currentEntropy + "\n" +str(self.totalEntropy))

        #Clear current recommendations for new recommendations to be displayed in solver frame
        for recommendation in self.delWidgets:
            recommendation.destroy()

        """Probability and Entropy calculations top recommendations handler"""
        self.sortedWordValues, self.totalEntropy, self.trackerValidation = self.SolverCalc.WordValueCalc(self.curTotalwrds, self.curPosswrds, self.dictLWFreq, self.DL04)
    
    def solverDisplay(self):
        """Handles the display of the results from the solver algorithm in solver frame"""

        self.wordsRem = tk.StringVar()
        self.possWordsRem = tk.StringVar()
        self.curEntRem = tk.StringVar()

        self.sortedWordValues, self.totalEntropy, self.trackerValidation = self.SolverCalc.WordValueCalc(self.curTotalwrds, self.curPosswrds, self.dictLWFreq, self.DL04)
        
        self.TotalWordsCount = len(self.curTotalwrds)
        self.PossibleWordsCount = len(self.curPosswrds)
        
        self.wordsRem.set(self.totalWordsRemaining + "\n" + str(self.TotalWordsCount))
        self.possWordsRem.set(self.possibleOutcomeText + "\n" + str(self.PossibleWordsCount))
        self.curEntRem.set(self.currentEntropy + "\n" +str(self.totalEntropy))
        r = 6
        self.delWidgets = []
        if(self.gamestarted == True):
            if self.solver_bool.get() == True:
                self.solverTitle = tk.Message(self.solver_frame,text = self.Title, 
                                                    font = self.HeaderBig, justify = "center",
                                                    width = 180)
                self.wordsRemaining = tk.Message(self.solver_frame,textvariable= self.wordsRem, 
                                                    font = self.Header,justify = "center",
                                                    width = 180)
                self.curEnt = tk.Message(self.solver_frame,textvariable= self.curEntRem, 
                                                    font = self.Header, justify = "center",
                                                    width = 180)
                self.posWords = tk.Message(self.solver_frame,textvariable= self.possWordsRem, 
                                                    font = self.Header, justify = "center",
                                                    width = 180)
                self.curRecommendations = tk.Message(self.solver_frame, text = self.RecommendationHeader,
                                                     font = self.HeaderBig, width = 195)
                self.keyy = tk.Message(self.solver_frame, text = self.Key,
                                                     font = self.HeaderBig, width = 190)
                self.keyy1 = tk.Message(self.solver_frame, text = self.Key1,
                                                     font = self.KeyText, width = 190)
                self.keyy2 = tk.Message(self.solver_frame, text = self.Key2,
                                                     font = self.KeyText, width = 190)
                self.keyy3 = tk.Message(self.solver_frame, text = self.Key3,
                                                     font = self.KeyText, width = 190)
                self.solverTitle.grid(row =1, column = 1, padx = 5)
                self.wordsRemaining.grid(row =2, column = 1)
                self.posWords.grid(row = 3, column = 1)
                self.curEnt.grid(row = 4, column = 1)
                self.curRecommendations.grid(row = 5, column = 1, ipady = 10)
                self.keyy.grid(row = 16, column = 1, pady = 5)
                self.keyy1.grid(row = 17, column = 1)
                self.keyy2.grid(row = 19, column = 1)
                self.keyy3.grid(row = 20, column = 1)
                
                #Below code handles the word recommendations displaying aspect of the solver
                
                if len(self.sortedWordValues) < 10:
                    n = len(self.sortedWordValues)
                else:
                    n = 10

                topWords =  heapq.nlargest(n, self.sortedWordValues.items(), key=lambda item: item[1])

                if self.trackerValidation == False:
                    for key, value in topWords:
                        if key in self.curPosswrds:
                            isPossSolution = 'Yes'
                        else: 
                            isPossSolution = '        '
                        self.Recomendation = tk.Message(self.solver_frame, text = key + "                " + isPossSolution +"          " + 
                                                    str(round(value, 6)),
                                                    font = self.Header, width = 195)
                        self.Recomendation.grid(row = r, column = 1, sticky = 'e', padx = 5)
                        self.delWidgets.append(self.Recomendation)
                        r += 1
                else:
                    for key,value in self.sortedWordValues.items():
                        if key in self.curPosswrds:
                            if len(self.curPosswrds) == 2:
                                self.sortedWordValues[key] = 0.50000
                            elif len(self.curPosswrds) == 1:
                                self.sortedWordValues[key] = 1.00000
                            isPossSolution = 'Yes'
                            self.Recomendation = tk.Message(self.solver_frame, text = key + "                " + isPossSolution +"          " + 
                                                    str(round(self.sortedWordValues[key], 6)),
                                                    font = self.Header, width = 195)
                            self.Recomendation.grid(row = r, column = 1, sticky = 'e', padx = 5)
                            self.delWidgets.append(self.Recomendation)
                            r += 1
