#initalize dictionary for the tracking of occurrences for specific letters in specific 
#spots of the five letter words 
#Example: {A: [], B: []} which will become {A: [40, 32, 19, 24, 3], B: [13, 46, 92, 8, 29]}
f = open("long_wordlist.txt", "r")
dict = {}

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetLength = 26

#initialize dict
for ch in alphabet:
    dict[ch.upper()] = []


for line in f:
    track = 0
    for char in line:
        dict[char][track] +=1 
        track += 1
    
print(dict)
