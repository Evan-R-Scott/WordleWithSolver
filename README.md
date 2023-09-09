# WordleRepo

Wordle.py - Wordle imitation program that is fully functional utilizing Tkinter which is Python's GUI interface.
It incorporates an optional solving algorithm which adapts based on information gain from previous guesses
to recommend the most optimal/value-driven guesses based on a number of factors.
Concepts/Factors incorporated in this Solver: 
- Entropy - average level of uncertainty/unknown information remaining based on possible outcomes
  (In terms of Wordle application, this can be viewed as the possible solutions we have remaining and how many steps
  it would take to get down to 1 word remaining (the Wordle answer))
- Information Theory/Information Gain - the minization of entropy/uncertainty in as short of steps as possible
- Tested data sets - (such as) frequency of letters in the english language and location of these said letters in a 5 letter word
- Renormalization - refactoring of probabilities for summation of 1 as letter information is gained from guessing words

Solver.py - Modularized code for Solver Algorithm utilized by Wordle.py program only if the user desires the assistance by the Solver

SolverCalculations.py -  Class utilized by solver algorithm containing methods of calculations for the value/weight of a word and current sum entropy which assists
in the word recommendation process utilized by the solver

DictionariesInGraphs.py - This file contains the contents for creating the bar graph/plot which visualizes the range of 
probabilities for both the general letter frequency dictionary and the letter in specific locations (of a 5 letter word)
frequencies dictionary 

DatasetDictionaryInitialization.py - This program initializes the dictionaries and scales the 2 datasets: LetterFrequency.txt and Long_wordlist.txt
