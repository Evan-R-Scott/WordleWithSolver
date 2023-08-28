"""                      RUN ME FOR Initial Dataset Dictionaries            """

#import statements
import csv

class DataProbCalc:
    def __init__(self):
        pass

#open files to be read
f = open("/Users/evanp/OneDrive/Desktop/Individual Projects/WordleRepo/long_wordlist.txt", "r")
d = open("/Users/evanp/OneDrive/Desktop/Individual Projects/WordleRepo/LetterFrequency.txt", "r")
csv_reader = csv.reader(d, delimiter = ',')

#create dictionaries
dictLWFreq = {}
totalLettersdictLWFreq = {}
dictLetterFreq = {}
totalLetters = 0

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

        totalLetters +=1

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

for key, value in totalLettersdictLWFreq.items():
    totalLettersdictLWFreq[key] = (round(value / totalLetters, 7))

#so print doesn't execute when running program for creating graphs
if __name__ == '__main__':
    #print final dictionaries
    print("\nDictionary for probability of letter frequency in all english words is:\n",dictLetterFreq)
    print("\nDictionary for probability of letter in a specific location is:\n" , dictLWFreq)
    print("\nDictionary for probability of letter frequency in 5 letter words is:\n", totalLettersdictLWFreq)
