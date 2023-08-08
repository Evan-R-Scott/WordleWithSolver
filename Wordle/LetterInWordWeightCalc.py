""" BY EVAN SCOTT"""
#This program scales the data set: Long_wordlist.txt down to a 0 to
# 1 range >>> explanation below 

#Long_wordlist.txt - initalize dictionary for the tracking of occurrences for 
# specific letters in specific spots of the five letter words 
#divide by the total occurrences of that letter in the list so each probability
#for each letter in different spots sums to 1 and then apply 
# sigmoid for proportionality across data set scaling
#Example: {A: [], B: []} which will become {A: [40, 32, 19, 24, 3], B: [13, 46, 92, 8, 29]}
#and finally(assuming probability of a letter being in each spot is equal) 
# {A: [0.2, 0.2, 0.2, 0.2, 0.2], B: [0.2, 0.2, 0.2, 0.2, 0.2]}

f = open("/Users/evanp/OneDrive/Desktop/Individual Projects/WordleRepo/Wordle/long_wordlist.txt", "r")
dict = {}
totalLettersDict = {}

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetLength = 26

#track how many of each letter there is


#initialize dict
for ch in alphabet:
    dict[ch.upper()] = [0,0,0,0,0]
    totalLettersDict[ch.upper()] = 0


for line in f:
    track = 0
    for char in line:
        chKey = char.upper()

        if char == "\n":
            continue

        totalLettersDict[chKey] +=1

        if dict[chKey][track] == 0:
            dict[chKey][track] = 1
        else:
            dict[chKey][track] +=1 
            track += 1

i = 0
for key, value  in dict.items():
    while i < 5:
        value[i] = (int(value[i]) / totalLettersDict[key])
        i+= 1
    i = 0

print(dict)
