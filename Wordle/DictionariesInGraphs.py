"""                RUN ME FOR Graphs of the Dataset Dictionaries             """
#This file contains the contents for creating the bar graph/plot which display the 
#range of probabilities for visual display of the Letter Frequency dictionary 
#and Letter in Specific Locations dictionary 

#Utilizes pandas and matplotlib

#import statements
import matplotlib.pyplot as plt
import pandas as pd
import DatasetDictionaryInitialization

#import dictionaries from DataProbabiityCalculation.py file
dictLWFreq =  DatasetDictionaryInitialization.dictLWFreq
dictLetterFreq = DatasetDictionaryInitialization.dictLetterFreq

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

#graph Letter Frequencies probabilities
x_valuesL = list(dictLetterFreq.keys())
y_valuesL = list(dictLetterFreq.values())

plt.bar(x_valuesL, y_valuesL, color = colors, width = 0.4)
plt.title('Letter Frequencies in English words')
plt.xlabel('Letters')
plt.ylabel('Probability')

#graph Letters in Specific Locations probabilities
y_valuesLInW = list(dictLWFreq.values())

tempIndex2 = ['A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O',
             'P','Q','R','S','T','U','V','W','X','Y','Z']
plotData = pd.DataFrame(y_valuesLInW, index = tempIndex2)
plotData.plot(kind = "bar", figsize = (8,6))
plt.title("Letter Occurrences in Specific Locations")
plt.xlabel("Letters")
plt.ylabel("Probability")


plt.show()