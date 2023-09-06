# WordleRepo

Wordle.py - Wordle imitation program that is fully functional utilizing Tkinter which is Python's GUI interface.
It incorporates an optional solving algorithm which adapts based on information gain from previous guesses
to recommend the most optimal/value-driven guesses based on a number of factors.
Concepts/Factors incorporated in this Solver: 
- Entropy - average level of uncertainty/unknown information remaining based on possible outcomes
  (In terms of Wordle application, this can be viewed as the possible solutions we have remaining and how many steps
  it would take to get down to 1 word remaining (the Wordle answer)
- Information Theory/Information Gain - the minization of entropy/uncertainty in as short of steps as possible
- Tested data sets - (such as) frequency of letters in the english language and location of these said letters in a 5 letter word
- Renormalization - refactoring of probabilities for summation of 1 as letter information is gained from guessing words

Solver.py - Modularized code for Solver Algorithm utilized by Wordle.py program only if the user desires the assistance by the Solver

SolverCalculations.py -  Class utilized by solver algorithm containing methods of calculations for the value/weight of a word and current sum entropy which assists
in the word recommendation process utilized by the solver

DictionariesInGraphs.py - This file contains the contents for creating the bar graph/plot which visualizes the range of 
probabilities for both the general letter frequency dictionary and the letter in specific locations (of a 5 letter word)
frequencies dictionary 

DatasetDictionaryInitialization.py - This program initializes the dictionaries and scales the 2 datasets: LetterFrequency.txt and Long_wordlist.txt down to a 0 to
1 range >>> explanation below 

  **Long_wordlist.txt - initalize dictionary ({key: [letter 1, letter 2, ... letter 5]}) for
  the tracking of occurrences for 
  specific letters in specific spots of the five letter words 
  divide by the total occurrences of that letter in the list so each probability
  for each letter in different spots sums to 1 for proportionality across data set scaling
  Example: {A: [], B: []} which will become {A: [40, 32, 19, 24, 3], B: [13, 46, 92, 8, 29]}
  and resulting in something such as (not accurate just as example): 
  {A: [0.12, 0.34, 0.04, 0.22, 0.006], B: [0.54, 0.22, 0.04, 0.11, 0.09]}

  **LetterFrequency - initialize dictionary ({key: frequency weight value of letter occurring})
  and divide those experiment-calculated values by total letter occurrences to get the summation of all 
  probabilities for all letters to be 1 for proportionality across data set scaling
  Example: {A: 0.24, B: 0.06, C: 0.19, ..., Z: 0.005} and this will sum to == 1 like the other dictionary
