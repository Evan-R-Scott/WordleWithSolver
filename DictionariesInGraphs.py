"""                RUN ME FOR Graphs(Found in Graphs Folder) of the initial dictionaries  of datasets            """

#import statements
import matplotlib.pyplot as plt
import pandas as pd
import DatasetDictionaryInitialization

#import dictionaries from DataProbabiityCalculation.py file
dictLWFreq =  DatasetDictionaryInitialization.dictLWFreq
dictLetterFreq = DatasetDictionaryInitialization.dictLetterFreq


"""Graph of General Letter Frequencies"""

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

DataFrame = pd.DataFrame(list(dictLetterFreq.items()), columns=['Letters', 'Probability'])

ax = DataFrame.plot(kind='bar', x='Letters', y='Probability', color=colors, width=0.4, legend=False)

ax.set_title('Letter Frequencies in English words')
ax.set_xlabel('Letters')
ax.set_ylabel('Probability')

# Display chart
plt.show()

"""Graph of Letters in Specific Locations Frequencies"""

y_valuesLInW = list(dictLWFreq.values())

tempIndex2 = ['A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O',
             'P','Q','R','S','T','U','V','W','X','Y','Z']

plotData = pd.DataFrame(y_valuesLInW, index = tempIndex2)
bx = plotData.plot(kind = "bar", figsize = (8,6))

bx.set_title("Letter Occurrences in Specific Locations")
bx.set_xlabel("Letters")
bx.set_ylabel("Probability")

# Display chart
plt.show()