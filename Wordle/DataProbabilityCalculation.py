#This program scales the 2 data set: LetterFrequency.txt and Long_wordlist.txt down to a 0 to
# 1 range >>> explanation below 

#Long_wordlist.txt - initalize dictionary ({key: [letter 1, letter 2, ... letter 5]}) for
#the tracking of occurrences for 
# specific letters in specific spots of the five letter words 
#divide by the total occurrences of that letter in the list so each probability
#for each letter in different spots sums to 1 for proportionality across data set scaling
#Example: {A: [], B: []} which will become {A: [40, 32, 19, 24, 3], B: [13, 46, 92, 8, 29]}
#and finally(assuming probability of a letter being in each spot is equal) 
# {A: [0.2, 0.2, 0.2, 0.2, 0.2], B: [0.2, 0.2, 0.2, 0.2, 0.2]}

#LetterFrequency (simpler) - initialize dictionary ({key: frequency weight value of letter occurring})
# and divide those experiment-calculated values by 100 to get the summation of all 
# probabilities  for all letters to be 1 for proportionality across data set scaling
#Example: {A: 0.24, B: 0.06, C: 0.19}

#import statements
import csv

class DataProbCalc:
    def __init__(self):
        pass

#open files to be read
f = open("/Users/evanp/OneDrive/Desktop/Individual Projects/WordleRepo/Wordle/long_wordlist.txt", "r")
d = open("/Users/evanp/OneDrive/Desktop/Individual Projects/WordleRepo/Wordle/LetterFrequency.txt", "r")
csv_reader = csv.reader(d, delimiter = ',')

#create dictionaries
dictLWFreq = {}
totalLettersdictLWFreq = {}
dictLetterFreq = {}

#variables for key initialization in dictionaries
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetLength = 26

#initialize dictLWFreq (dictionary letters in words frequency)
for ch in alphabet:
    dictLWFreq[ch.upper()] = [0,0,0,0,0]
    totalLettersdictLWFreq[ch.upper()] = 0

#create dictionary for dictLetterFreq(dictionary for letters frequency)
for line in csv_reader:
    dictLetterFreq[line[0]] = (float(line[1]) / 100.0)

#loop through the file line by line and char by char for summation of all occurrences of letters in
#specific places in the 5 letter word placed in dictionary values which is a 5 length list for 
#each respective letter position
for line in f:
    track = 0
    for char in line:
        chKey = char.upper()

        if char == "\n":
            continue

        totalLettersdictLWFreq[chKey] +=1

        if dictLWFreq[chKey][track] == 0:
            dictLWFreq[chKey][track] = 1
        else:
            dictLWFreq[chKey][track] +=1 
            track += 1

i = 0
#loop through dictLWFreq and calculate probability a letter is in each specific spot of word
#by dividing times that letter occurred in that spot by total times that letter occurred
for key, value  in dictLWFreq.items():
    while i < 5:
        value[i] = (round((int(value[i]) / totalLettersdictLWFreq[key]), 6))
        i+= 1
    i = 0

    def DictLetterFreq():
        return dictLetterFreq
    
    def DictLetterWordFreq():
        return dictLWFreq

#so print doesn't execute when running program for creating graphs
if __name__ == '__main__':
    #print final dictionaries
    print("\nDictionary for probability of letter frequency is:\n",dictLetterFreq)
    print("\nDictionary for probability of letter in a specific location is:\n" , dictLWFreq)
