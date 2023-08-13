"""
File: iteration2Helper.py
Author: COMP 120 instructor
Description: Code that illustrates putting widgets in frames.
"""
import DataProbabilityCalculation

import random
import tkinter as tk

import tkinter.font as font
import time

from enum import Enum
class Wordy:
    def __init__(self):
        
        self.variablesDontEdit()        #variables that do not affect game play
        self.variablesEdit()            #The universal Variables
        self.makeWrdLst()           #Makes all the words into a list
        self.setScreen()            #Builds the Screen
        self.gameScreen()           #Builds the game screen
        self.guessFrames()
        self.keyScreen()            #Builds the keyboard frame
        self.keybuttons()
        self.SolverInfo()
        self.messageScreen()        #Presents messages to the user
        self.parameterScreen()      #The Parameter Screen
        self.buttonFrame()           #Houses start and quit button    
        
        #Change size of screen and spacing
    def variablesDontEdit(self):
        """Variables used thorughout the program that don't affect the visuals"""
        self.gamestarted = False
        self.runChecks = 'normal'
        self.text = ''
        self.answer = ''
        self.buttons = {}
        self.curColumn = 1
        self.curRow = 1
        self.curGuess = ''

    def variablesEdit(self):
        # Constants
        self.WORD_SIZE = 5  # number of letters in the hidden word
        self.NUM_GUESSES = 6 # number of guesses that the user gets 
        self.LONG_WORDLIST_FILENAME = "/Users/evanp/OneDrive/Desktop/Individual Projects/WordleRepo/Wordle/long_wordlist.txt"
        self.SHORT_WORDLIST_FILENAME = "/Users/evanp/OneDrive/Desktop/Individual Projects/WordleRepo/Wordle/short_wordlist.txt"

        #Initialize the list containing 5 dictionaries for each specific spot with letters and probabilities
        #that get removed and renormalised bsaed on guess making letters green/gray/yellow
        self.DL04 =  []
        for _ in range(5):
            self.DL04.append(DataProbabilityCalculation.dictLetterFreq)

        self.dictLetterFreqVals = DataProbabilityCalculation.dictLetterFreq
        print(self.dictLetterFreqVals)
        lst4 = self.dictLetterFreqVals.values()
        self.curProb = sum(lst4)
        print(self.curProb)
        print('\n')
        self.dictLWFreq = DataProbabilityCalculation.dictLWFreq

        # Size of the frame that holds all guesses.  This is the upper left
        # frame in the window.
        self.PARENT_GUESS_FRAME_WIDTH = 750
        self.PARENT_GUESS_FRAME_HEIGHT = 400

        # Parameters for an individual letter in the guess frame
        # A guess frame is an individual box that contains a guessed letter.
        self.GUESS_FRAME_SIZE = 50  # the width and height of the guess box.
        self.GUESS_FRAME_PADDING = 3 
        self.GUESS_FRAME_BG_BEGIN = 'white' # background color of a guess box 
                                            # after the user enters the letter,
                                            # but before the guess is entered.
        self.GUESS_FRAME_TEXT_BEGIN = 'black' # color of text in guess box after the
                                            # user enters the letter, but before
                                            # the guess is entered.
        self.GUESS_FRAME_BG_WRONG = 'grey'  # background color of guess box
                                            # after the guess is entered, and the
                                            # letter is not in the hidden word.
        self.GUESS_FRAME_BG_CORRECT_WRONG_LOC = 'orange' # background color
                                            # guess box after the guess is entered
                                            # and the letter is in the hidden word
                                            # but in the wrong location.
        self.GUESS_FRAME_BG_CORRECT_RIGHT_LOC = 'green' # background color
                                            # guess box after the guess is entered
                                            # and the letter is in the hidden word
                                            # and in the correct location.
        self.GUESS_FRAME_TEXT_AFTER = 'white' # color of text in guess box after
                                            # the guess is entered.
        self.FONT_FAMILY = 'ariel'          # Font to use for letters in the guess boxes.
        self.FONT_SIZE_GUESS = 35           # Font size for letters in the guess boxes.

        #initialize entropy value to 0
        self.curEntropyVal = 0

        #Trackers for Green/Yellow/Gray Letters
        self.correctLetters = [0,0,0,0,0]
        self.grayLetters = []
        self.totalGrayLetters = []
        self.grayRenormalizationProb = [0,0,0,0,0]
        self.tempLocYellow = [[],[],[],[],[]]

        #solver variables
        self.FontHeader = 8
        self.FontRecommendations = 4
        self.Header = (self.FONT_FAMILY, self.FontHeader)
        self.HeaderBig = (self.FONT_FAMILY, self.FontHeader, 'bold')
        self.Title = "Solver"
        self.totalWordsRemaining = "Total Pool of Words Remaining:"
        self.currentEntropy = "Current Entropy/Uncertainty:"
        self.possibleOutcomeText = "Potential Answers Remaining:"
        self.RecommendationHeader = "Top Picks      ||   E[Info]   ||   P(word)"
        self.SolverFrameWidth = 200

        self.restartGame = False


        # Parameters for the keyboard frame
        self.KEYBOARD_FRAME_HEIGHT = 200
        self.KEYBOARD_BUTTON_HEIGHT = 2
        self.KEYBOARD_BUTTON_WIDTH = 3  # width of the letter buttons.  Remember,
                                        # width of buttons is measured in characters.
        self.KEYBOARD_BUTTON_WIDTH_LONG = 5 # width of the enter and back buttons.

        # The following colors for the keyboard buttons
        # follow the same specifications as the colors defined above for the guess
        # boxes.  The problem is that at least on macs, in Tkinter you cannot change
        # the background color of a button.  So you will leave the background color as the
        # default (white),and just change the color of the text in the button, 
        # instead of the background color.
        # So the text color starts as the default (black), and then changes to grey, orange, 
        # green depending on the result of the guess for that letter.
        self.KEYBOARD_BUTTON_TEXT_BEGIN = 'black' 
        self.KEYBOARD_BUTTON_TEXT_WRONG = 'grey'  
        self.KEYBOARD_BUTTON_TEXT_CORRECT_WRONG_LOC = 'orange' 
        self.KEYBOARD_BUTTON_TEXT_CORRECT_RIGHT_LOC = 'green' 

        self.KEYBOARD_BUTTON_NAMES = [   
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["ENTER", "Z", "X", "C", "V", "B", "N", "M", "BACK"]]
        
        # Parameters for the control frame
        self.CONTROL_FRAME_HEIGHT = self.PARENT_GUESS_FRAME_HEIGHT + self.KEYBOARD_FRAME_HEIGHT
        self.CONTROL_FRAME_WIDTH = 300
        self.USER_SELECTION_PADDING = 10  # Horizontal padding on either side of the widgets in
                                            # the parameter frame.

        self.MESSAGE_DISPLAY_TIME_SECS = 5 # Length of time the message should be
                                            # displayed.

                                        # When processing a guess (changing color
                                        # of the guess frames), time to wait between
        self.PROCESS_GUESS_WAITTIME = 1  # updating successive frames.
    
    def makeWrdLst(self):
        """
        Reads through the lists of words provided and makes them into a list for later usages
        """
        self.longwrd = []   #Creates a list of all the words
        f = open( self.LONG_WORDLIST_FILENAME, 'r')
        for wrd in f:
            self.longwrd.append(wrd.strip())
        f.close()

        self.TotalWordsCount = len(self.longwrd)

        self.shortwrd = []  #Creates a list of all words the wordle can use
        f = open(self.SHORT_WORDLIST_FILENAME, 'r')
        for wrd in f:
            self.shortwrd.append(wrd.strip())
        f.close()

        self.PossibleWordsCount = len(self.shortwrd)

    def setScreen(self):
        """
        Creates the entire window for wordle 
        """
        # Create window
        self.window = tk.Tk()
        self.window.title("Wordy")

        # Control Frame
        self.conrtol = tk.Frame(self.window, 
            relief = 'solid',
            height = self.CONTROL_FRAME_HEIGHT, width = self.CONTROL_FRAME_WIDTH)
        self.conrtol.grid(row = 1, column = 3, rowspan = 2)
        self.conrtol.grid_propagate(False)

        # Solver Frame
        self.solver_frame = tk.Frame(self.window, 
            borderwidth = 1, relief = 'solid',
            height = self.PARENT_GUESS_FRAME_HEIGHT, width = self.SolverFrameWidth)
        self.solver_frame.grid(row = 1, column = 1)
        self.solver_frame.grid_propagate(False)

    def gameScreen(self):
        """Create the game play frame"""
        self.game_frame = tk.Frame(self.window, 
            borderwidth = 1, relief = 'solid',
            height = self.PARENT_GUESS_FRAME_HEIGHT, width = self.PARENT_GUESS_FRAME_WIDTH)
        self.game_frame.grid(row = 1, column = 2)
        self.game_frame.grid_propagate(False)

    def guessFrames(self):
        """The game play screen where the guesses are displayed"""
        for r in range(self.NUM_GUESSES):
            for c in range(self.WORD_SIZE):
                frames  = tk.Frame(self.game_frame,
                        borderwidth = 1, relief = 'solid',
                        width = self.GUESS_FRAME_SIZE,
                        height= self.GUESS_FRAME_SIZE,
                        bg=self.GUESS_FRAME_BG_BEGIN)
                frames.grid(row = r + 1, column = c + 1, padx = self.GUESS_FRAME_PADDING, pady= self.GUESS_FRAME_PADDING)
                

                
        self.game_frame.rowconfigure(0, weight = 1)
        self.game_frame.rowconfigure(self.NUM_GUESSES + 1, weight = 1)
        self.game_frame.columnconfigure(0, weight = 1)
        self.game_frame.columnconfigure(self.WORD_SIZE + 1, weight = 1)

    def keyScreen(self):
        #Key Frame
        self.key_frame = tk.Frame(self.window, 
            borderwidth = 1, relief = 'solid',
            height = self.KEYBOARD_FRAME_HEIGHT, width = self.PARENT_GUESS_FRAME_WIDTH)
        self.key_frame.grid(row = 2, column = 2)
        self.key_frame.grid_propagate(False)

    def keybuttons(self):
        """Displays the buttons onto key screen"""
        for r in range(len(self.KEYBOARD_BUTTON_NAMES)):
            for c in range(len(self.KEYBOARD_BUTTON_NAMES[r])):

                # Define a handler for this button.
                # Note that functions can be dynamically 
                # defined, as is happening here.  Each
                # button gets its own hander.  
                # But each handler calls the same method
                # (button_handler), but with a parameter
                # that specifies which button was pressed.
                
                def handler(key = self.KEYBOARD_BUTTON_NAMES[r][c]):
                    self.button_handler(key)
                button = tk.Button(self.key_frame,
                        width = self.KEYBOARD_BUTTON_WIDTH,
                        height= self.KEYBOARD_BUTTON_HEIGHT,
                        text = self.KEYBOARD_BUTTON_NAMES[r][c],
                        fg=self.KEYBOARD_BUTTON_TEXT_BEGIN, 
                        font=self.FONT_FAMILY,
                        command = handler)
                button.grid(row = r + 1, column = c + 1, padx = 10 )

                    # Put the button in a dictionary of buttons
                    # where the key is the button text, and the
                    # value is the button object.
                self.buttons[self.KEYBOARD_BUTTON_NAMES[r][c]] = button
                
                    
        self.buttons['ENTER']['width'] = self.KEYBOARD_BUTTON_WIDTH_LONG
        self.buttons['BACK']['width'] = self.KEYBOARD_BUTTON_WIDTH_LONG
        self.buttons['ENTER']['command'] = self.enterHandler
        self.buttons['BACK']['command'] = self.backHandler

        # Center the grid of buttons in the button frame
        self.key_frame.rowconfigure(0, weight = 1)
        self.key_frame.rowconfigure(len(self.KEYBOARD_BUTTON_NAMES) + 1, weight = 1)
        self.key_frame.columnconfigure(0, weight = 1)
        self.key_frame.columnconfigure(len(self.KEYBOARD_BUTTON_NAMES[0]) + 1, weight = 1)

    def button_handler(self, text):
        """
        Changes the color of the button that was pressed
        """ 
        if(self.curColumn <= self.WORD_SIZE and self.curRow -1 < self.NUM_GUESSES and self.gamestarted == True):
            #self.buttons[text]['fg'] = self.KEYBOARD_BUTTON_TEXT_WRONG
            let = tk.Message(self.game_frame, text= text, font=self.FONT_FAMILY, aspect= self.FONT_SIZE_GUESS, bg= 'white')
            let.grid(row= self.curRow, column= self.curColumn)
            self.curColumn += 1
            self.curGuess += text
    def backHandler(self):
        """If back is pressed erases the letters"""
        if(self.curColumn > 1 and self.gamestarted == True):
            self.curColumn -= 1
            let = tk.Message(self.game_frame, text= ' ', font=self.FONT_FAMILY, aspect= self.FONT_SIZE_GUESS, bg = 'white')
            let.grid(row= self.curRow, column= self.curColumn)
            self.curGuess = self.curGuess[0:-1]
    def enterHandler(self):
        """Handle what happens when enter is pressed; it is not a word, it is too short, it is the right answer or all guesses are used up"""
        if self.curRow == self.NUM_GUESSES:
            self.gamestarted = False
            self.messageString.set('Guesses used up. Word was: ' + self.answer + '. Game over.' + '\n\n' + 'Would you like to play again?')
            self.restartGame = True
            self.startBTN.set("Play Again")
        elif self.answer == self.curGuess:
            time.sleep(self.PROCESS_GUESS_WAITTIME)
            self.displayEntered()
            self.gamestarted = False
            self.messageString.set('Correct. Nice job. Game over' + '\n\n' + 'Would you like to play again?')
            self.restartGame = True
            self.startBTN.set("Play Again")
        elif(self.curRow <= self.NUM_GUESSES and self.gamestarted == True):
            if(str.lower(self.curGuess) in self.longwrd and self.guess_type_bool.get() == True and self.curColumn-1 == self.WORD_SIZE):
                time.sleep(self.PROCESS_GUESS_WAITTIME)
                self.displayEntered()
                self.curRow += 1
                self.curColumn = 1
                self.curGuess = ''
            elif(self.guess_type_bool.get() == False and self.curColumn-1 == self.WORD_SIZE):
                time.sleep(self.PROCESS_GUESS_WAITTIME)
                self.displayEntered()
                self.curRow += 1
                self.curColumn = 1
                self.curGuess = ''
            elif(self.guess_type_bool.get() == True and self.curColumn-1 == self.WORD_SIZE):
                self.messageString.set('Word is not in the guess list')
                self.window.after(self.MESSAGE_DISPLAY_TIME_SECS*1000, self.remove_message)
            else: #Word is not long enough
                self.messageString.set('Word is not long enough')
                self.window.after(self.MESSAGE_DISPLAY_TIME_SECS*1000, self.remove_message)
    
    #renormalize the probabilities of letters in 5 dictionaries because letters got removed
    #from previous guess
    def renormalization(self):
            scalingGFactor = [0,0,0,0,0]
            print(self.grayRenormalizationProb)
            for i in range(5):
                scalingGFactor[i] = 1 / 1 - self.grayRenormalizationProb[i]
            curG = 0
            for dictionary in self.DL04:
                if len(dictionary) > 1:
                    for key in dictionary:
                        if key not in self.grayLetters:
                            dictionary[key] = round((dictionary[key]  * scalingGFactor[curG]), 6)
                lst1 = dictionary.values()
                print(sum(lst1))
                curG += 1
            self.grayRenormalizationProb = [0,0,0,0,0]
            self.grayLetters = []

    def displayEntered(self):
        """
        Creates a dictionary of the letters and keys and the number of occurances and makes sure that is a letter occurs 
        multiples times it will go yellow multipule times, also handles the color transformation of the keyboard.
        """
        guessDic = {} #keys as letters and values as number of occurances
        answerDic = {}
        lst1 = []
        lst2 = []
        for i in range(len(self.curGuess)): #makes back ground green if right let and loc otherwise adds a dictionary of letters in guess and 
            lst1.append(i+1)
            if(self.curGuess[i] == self.answer[i]): #turns the color green
                lst2.append(i+1)
                #keeps track of where correct letters are located when found so we can test other uncertain letters
                #in that already determined location's answer
                self.correctLetters[i] = self.curGuess[i]
                #sets value/probability to 1 and removes all other letters from that list because found correct letter in
                #correct spot
                #self.DL04[i][self.curGuess[i]]
                self.DL04[i] = {self.correctLetters[i]: 1.0}

                frames  = tk.Frame(self.game_frame,
                            borderwidth = 1, relief = 'solid',
                            width = self.GUESS_FRAME_SIZE,
                            height= self.GUESS_FRAME_SIZE,
                            bg=self.GUESS_FRAME_BG_CORRECT_RIGHT_LOC)
                frames.grid(row = self.curRow, column = i + 1, padx = self.GUESS_FRAME_PADDING, pady= self.GUESS_FRAME_PADDING)
                let = tk.Message(self.game_frame, text= self.curGuess[i], font=self.FONT_FAMILY, 
                            aspect= self.FONT_SIZE_GUESS, fg= 'white', bg= self.GUESS_FRAME_BG_CORRECT_RIGHT_LOC)
                let.grid(row= self.curRow, column= i + 1)
                self.buttons[self.curGuess[i]]['fg'] = self.GUESS_FRAME_BG_CORRECT_RIGHT_LOC
            else:
                if(self.curGuess[i] in guessDic):
                    guessDic[self.curGuess[i]] += 1
                else:
                    guessDic[self.curGuess[i]] = 1

                if(self.answer[i] in answerDic):
                    answerDic[self.answer[i]] += 1
                else:
                    answerDic[self.answer[i]] = 1

        for i in guessDic.keys(): #looks through the dictionary containing letters in the guess and the number of times it occurs and adds yellow frames
            if i in answerDic.keys():
                if guessDic[i] > answerDic[i]:
                    num = answerDic[i]
                else:
                    num = guessDic[i]
                for t in range(len(self.curGuess)):
                    #if num > 0:
                        if self.curGuess[t] != self.answer[t] and self.curGuess[t] in answerDic.keys():
                            
                            if (self.curGuess[t] not in self.tempLocYellow[t] and (len(self.DL04[t]) > 1)):
                                    self.tempLocYellow[t].append(self.curGuess[t])
                                    self.grayRenormalizationProb[t] += self.DL04[t][self.curGuess[t]]
                                    self.DL04[t] = {key: self.DL04[t][key] for key in self.DL04[t]
                                                    if key != self.curGuess[t]}
                                    self.renormalization()
                        if self.curGuess[t] != self.answer[t] and self.curGuess[t] == i:
                            frames  = tk.Frame(self.game_frame,
                                        borderwidth = 1, relief = 'solid',
                                        width = self.GUESS_FRAME_SIZE,
                                        height= self.GUESS_FRAME_SIZE,
                                        bg=self.GUESS_FRAME_BG_CORRECT_WRONG_LOC)
                            frames.grid(row = self.curRow, column = t + 1, padx = self.GUESS_FRAME_PADDING, pady= self.GUESS_FRAME_PADDING)
                            let = tk.Message(self.game_frame, text= self.curGuess[t], font=self.FONT_FAMILY, 
                                        aspect= self.FONT_SIZE_GUESS, fg= 'white', bg= self.GUESS_FRAME_BG_CORRECT_WRONG_LOC)
                            let.grid(row= self.curRow, column= t + 1)
                            num -= 1
                            lst2.append(t+1)
                            self.buttons[self.curGuess[t]]['fg'] = self.GUESS_FRAME_BG_CORRECT_WRONG_LOC

        #save gray letters to be removed from letter dictionaries in specific spots
        for ch in self.curGuess:
            if ch not in self.answer and ch not in self.totalGrayLetters:
                for i in range(5):
                    if ((len(self.DL04[i]) != 1)):
                        self.grayRenormalizationProb[i] += self.DL04[i][ch]
                self.totalGrayLetters.append(ch)
                self.grayLetters.append(ch)

        for dictionary in self.DL04:
            for ch in self.grayLetters:
                if ch in dictionary:
                    del dictionary[ch]
            #dictionary = {key: dictionary[key] for key in dictionary if key not in self.grayLetters}

        for i in lst1: #if it has not changed colors then it will go grey
            if i not in lst2:
                frames  = tk.Frame(self.game_frame,
                                            borderwidth = 1, relief = 'solid',
                                            width = self.GUESS_FRAME_SIZE,
                                            height= self.GUESS_FRAME_SIZE,
                                            bg=self.GUESS_FRAME_BG_WRONG)
                frames.grid(row = self.curRow, column = i, padx = self.GUESS_FRAME_PADDING, pady= self.GUESS_FRAME_PADDING)
                let = tk.Message(self.game_frame, text= self.curGuess[i-1], font=self.FONT_FAMILY, 
                                aspect= self.FONT_SIZE_GUESS, fg= 'white', bg= self.GUESS_FRAME_BG_WRONG)
                let.grid(row= self.curRow, column= i)
                self.buttons[self.curGuess[i-1]]['fg'] = self.GUESS_FRAME_BG_WRONG

        self.renormalization()
    def SolverInfo(self):
        self.curInfoFrame = tk.Frame(self.solver_frame, borderwidth = 1, relief = 'solid',
                                     height = self.CONTROL_FRAME_HEIGHT,
                                     width = self.SolverFrameWidth)
        self.curInfoFrame.grid(row = 1, column = 1)
        self.curInfoFrame.grid_propagate(False)
       
    def messageScreen(self):
        # Message Frame
        self.messageString = tk.StringVar()
        self.messageFrame = tk.Frame(self.conrtol, borderwidth = 1, relief = 'solid',
            height = self.CONTROL_FRAME_HEIGHT/3, width = self.CONTROL_FRAME_WIDTH)
        self.messageFrame.grid(row = 1, column = 1)
        self.messageFrame.grid_propagate(False)
        self.message = tk.Message(self.messageFrame, textvariable= self.messageString, justify = 'center', width= self.CONTROL_FRAME_WIDTH)
        self.message.grid(row= 1, column=1)
        self.messageFrame.rowconfigure(0, weight=1)
        self.messageFrame.rowconfigure(2, weight=1)
        self.messageFrame.columnconfigure(0, weight=1)
        self.messageFrame.columnconfigure(2, weight=1)

    def parameterScreen(self):
        if(self.gamestarted == False):
            self.specify_word_bool = tk.BooleanVar()
            self.specify_word_bool.set(False)
            self.guess_type_bool = tk.BooleanVar()
            self.guess_type_bool.set(True)
            self.show_word_bool = tk.BooleanVar()
            self.show_word_bool.set(False)
            self.solver_bool = tk.BooleanVar()
            self.solver_bool.set(False)

        # Parameter Frame
        self.parameter = tk.Frame(self.conrtol, 
            borderwidth = 1, relief = 'solid',
            height = self.CONTROL_FRAME_HEIGHT/3, width = self.CONTROL_FRAME_WIDTH)
        self.parameter.grid(row = 2, column = 1)
        self.parameter.grid_propagate(False)

        #Guesses must be words
        self.guess_type = tk.Checkbutton(self.parameter, text="Guesses must be words",
                            var = self.guess_type_bool, command = self.mustBeWord, state= self.runChecks)
        self.guess_type.grid(row = 1, column = 1, sticky = tk.W, pady = self.GUESS_FRAME_PADDING)

        #Show Word
        self.show_word = tk.Checkbutton(self.parameter, text="Show word", 
                            var = self.show_word_bool, command= self.display_answer)
        self.show_word.grid(row = 2, column = 1, sticky = tk.W, pady = self.GUESS_FRAME_PADDING)

        #display word
        self.displayWordString = tk.StringVar()
        self.displayWord = tk.Message(self.parameter, textvariable= self.displayWordString, width= self.CONTROL_FRAME_WIDTH//2)
        self.displayWord.grid(row= 2, column= 2)

        #Solver Option
        self.solver = tk.Checkbutton(self.parameter, text="Solver Assistance Algorithm", 
                            var = self.solver_bool, command = self.solverAlg, state = self.runChecks)
        self.solver.grid(row = 4, column = 1, sticky = tk.W, pady = self.GUESS_FRAME_PADDING)

        #specify Word
        self.specify_word = tk.Checkbutton(self.parameter, text="Specify word", 
                            var = self.specify_word_bool, state= self.runChecks)
        self.specify_word.grid(row = 3, column = 1, sticky = tk.W, pady = self.GUESS_FRAME_PADDING)

        #entry
        self.entry_var = tk.StringVar()
        self.entry  = tk.Entry(self.parameter, textvariable=self.entry_var, width = self.WORD_SIZE, state=self.runChecks)
        self.entry.grid(row = 3, column=2, padx = self.GUESS_FRAME_PADDING)

        #center check boxes
        self.parameter.grid_rowconfigure(0, weight= 1)
        self.parameter.grid_rowconfigure(4, weight= 1)
        self.parameter.grid_columnconfigure(0, weight= 1)
        self.parameter.grid_columnconfigure(3, weight= 1)

    def buttonFrame(self):
        """Button Frame"""
        self.button = tk.Frame(self.conrtol, 
            borderwidth = 1, relief = 'solid',
            height = self.CONTROL_FRAME_HEIGHT/3, width = self.CONTROL_FRAME_WIDTH)
        self.button.grid(row = 3, column = 1)
        self.button.grid_propagate(False)

        # Put a start button in the bottom frame
        self.startBTN = tk.StringVar()
        self.startBTN.set("Start Game")
        start_button  = tk.Button(self.button, height = 3, width = 10, textvariable = self.startBTN, command = self.start)
        start_button.grid(row = 1, column=1)

        # Put a quit button in the bottom frame
        quit_button  = tk.Button(self.button, height = 3, width = 10 ,text = "Quit", command = self.quit)
        quit_button.grid(row = 1, column=3)

        # Centers the button in its frame
        self.button.grid_rowconfigure(1, weight = 1)

        self.button.grid_columnconfigure(0, weight = 50)
        self.button.grid_columnconfigure(1, weight = 2)
        self.button.grid_columnconfigure(2, weight = 1)
        self.button.grid_columnconfigure(3, weight = 2)
        self.button.grid_columnconfigure(4, weight = 50)
        
        self.window.mainloop()

    #handles wordle solver algorithm
    def solverAlg(self):
        if(self.gamestarted == True):
            if self.solver_bool.get() == True:
                self.solverTitle = tk.Message(self.curInfoFrame,text = self.Title, 
                                                    font = self.HeaderBig, justify = "center",
                                                    width = 180)
                self.wordsRemaining = tk.Message(self.curInfoFrame,text = self.totalWordsRemaining + "\n" +
                                                 str(self.TotalWordsCount), 
                                                    font = self.Header,justify = "center",
                                                    width = 180)
                self.curEnt = tk.Message(self.curInfoFrame,text = self.currentEntropy + "\n" +
                                         str(self.curEntropyVal), 
                                                    font = self.Header, justify = "center",
                                                    width = 180)
                self.posWords = tk.Message(self.curInfoFrame,text = self.possibleOutcomeText + "\n" + str(self.PossibleWordsCount), 
                                                    font = self.Header, justify = "center",
                                                    width = 180)
                self.curRecommendations = tk.Message(self.curInfoFrame, text = self.RecommendationHeader,
                                                     font = self.HeaderBig, width = 190)
                self.solverTitle.grid(row =1, column = 1, padx = 5)
                self.wordsRemaining.grid(row =2, column = 1)
                self.posWords.grid(row = 3, column = 1)
                self.curEnt.grid(row = 4, column = 1)
                self.curRecommendations.grid(row = 5, column = 1, ipady = 10)

    #Handlers For Buttons and messages
    def mustBeWord(self):
        """If must be word is checked then it makes sure that the thing entered is a word"""
        if(self.gamestarted == True):
            if self.guess_type_bool.get() == False:
                self.guess_type.select()
            else:
                self.guess_type.deselect()

    def start(self):
        """Checks if game has been started if not look and see if it is in an exept condition else display message"""
        if(self.restartGame):
            self.window.destroy()
            Wordy()
        if(len(self.curGuess) == 0):
            self.display_answer()
            if(self.gamestarted == False):
                self.solverAlg()
                self.force_word_check()
                if(self.gamestarted == True):
                    self.runChecks = 'disabled'
                    self.parameterScreen()
            if(self.gamestarted == True):
                self.solverAlg()
                self.messageString.set('Game has started')
                self.window.after(self.MESSAGE_DISPLAY_TIME_SECS*500, self.remove_message)

    def quit(self):
        """destroy window"""
        self.window.destroy()

    def force_word_check(self):
        """Checks to see if user wants to assign a word and then if the length is valid"""
        if self.specify_word_bool.get() == True:
            if(len(self.entry.get()) != self.WORD_SIZE):
                self.messageString.set('Incorrect specified word length')
                self.window.after(self.MESSAGE_DISPLAY_TIME_SECS*1000, self.remove_message)
            elif(self.entry.get() not in self.longwrd and self.guess_type_bool.get() == True):
                self.messageString.set('Specified word not a valid word')
                self.window.after(self.MESSAGE_DISPLAY_TIME_SECS*1000, self.remove_message)
            else:
                self.answer = str.upper(self.entry.get())
                self.entry.delete(0,'end')
                self.gamestarted = True
        else:
            self.gamestarted = True
            self.pick_word()
        
    def pick_word(self):
        """randomly selcts a word from list"""
        self.answer = str.upper(random.choice(self.shortwrd))
        if(len(self.answer) != self.WORD_SIZE):
            self.pick_word()
        
    def display_answer(self):
        """shows answer word when toggled on"""
        if self.show_word_bool.get() == True:
            self.displayWordString.set(str.lower(self.answer))
        else:
            self.displayWordString.set('')

    def remove_message(self):
        """removes message string"""
        self.messageString.set('')


if __name__ == "__main__":
   Wordy()