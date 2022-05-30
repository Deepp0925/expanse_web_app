def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    return words

myarray=readFile("./experimentResults.txt") #reads the entire file in an array
#print(myarray)
for myline in myarray:      #reads the array "myarray" line by line
    #print(myline)
    items = myline.split()  #splits the line in tokens and stores them in the array "items"
    #print(items)
    if items[0] == "Dataset:":
        myflag = "Dataset"
        table1c1 = []
        table1c2 = []
        temp = []
    if items[0] == "Confusion":
        myflag = "Confusion"
        jump = 0
        confusionTable = []
        therow = []
    if items[0] == "Agregated":
        myflag = "Agregated"
        jump1 = 0
        table2c1 = []
        table2c2 = []
        temp0 = []
        temp1 = []
        myAccuracy = []
    if items[0] == "Kappa:":
        myflag = "Kappa"
        jump2 = 0
        myKappa = []
        table3c1 = []
        table3c2 = []

# Here start the dataset info
    if myflag == "Dataset":
        table1c2.append(items[-1])
        temp = []
        for i in range(0, len(items)-1):
             temp.append(items[i])
        table1c1.append(' '.join(temp))
        count = 0
        for myword in table1c1:
            if myword[-1] == ":":
                table1c1[count] = myword[:-1]
            count = count + 1          

# Here starts processing the Confusion Matrix
    if myflag == "Confusion":
        if jump == 0:
            jump = 1
        else:
            for i in range(0, len(items)):
                theitem = items[i]
                theitem=theitem.replace("]","")
                theitem=theitem.replace("-","")
                print(theitem)
                if theitem[0] == "[":
                    confusionTable.append(therow) 
                    therow = []
                    theitem=theitem.replace("[","")
                theitem = float(theitem)
                therow.append(theitem)

# Here starts processing the Aggregated values
    if myflag == "Agregated":
        if jump1 == 0:  # This skips the line "Agregated ..."
            jump1 = 1
        elif jump1 == 1: # This consider the line with total accuracy
            myAccuracy.append(items[0])
            temp0 = []
            for i in range(1, len(items)):
                temp0.append(items[i])
            myAccuracy.append(' '.join(temp0))
            jump1 = 2
        else:   #the rest of the lines in the "Agregated" group
            table2c1.append(items[0])
            temp1 = []
            for i in range(1, len(items)):
                #print(items[i])
                temp1.append(items[i])
            table2c2.append(' '.join(temp1))
            count = 0
            for myword in table2c1:
                if myword[-1] == ":":
                    table2c1[count] = myword[:-1]
                count = count + 1

# Here starts processing the last 3 lines of information
    if myflag == "Kappa":
        if jump2 == 0: # This handles the Kappa information 
            theitem=items[0].replace(":","")
            myKappa.append(theitem)
            temp0 = []
            for i in range(1, len(items)):
                temp0.append(items[i])
            myKappa.append(' '.join(temp0))
            jump2 = 1
        else: # This handles the performance information
            temp0 = []
            for i in range(0, 2):
                temp0.append(items[i])
            table3c1.append(' '.join(temp0))
            temp0 = []
            for i in range(3, len(items)):
                temp0.append(items[i])
            table3c2.append(' '.join(temp0))
   
# Import functions from other files for table plotting
from plotTable import plotMyTable
# Here start printing all tables
expHead=['<b>Experiment Parameters</b>', ' ']
expCell=[table1c1, table1c2]
plotMyTable(expHead,expCell,"experimentInfo.png")
print("Experiment Information")
print(table1c1) 
print(table1c2)
print("\n")

confusionTable.append(therow)
confusionTable.pop(0)
print("Confusion Matrix")
print(confusionTable)

# Here we plot the confusion matrix in a file
#==========
import seaborn as sns
import matplotlib.pyplot as plt

ax = plt.subplot()
#sns.heatmap(confusionTable, annot=True, cmap='Blues')
sns.heatmap(confusionTable, annot=True, ax = ax, fmt = 'g')
ax.set_title('Seaborn Confusion Matrix with labels\n\n');
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ');

## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
ax.yaxis.set_ticklabels(['1','2','3','4','5','6','7','8','9','10','11','12','13','14',    '15','16','17'])

## Display the visualization of the Confusion Matrix.
plt.show()

#==========
#import numpy as np
#from confusionMatrixPlot import plot_confusion_matrix

#plot_confusion_matrix(cm = np.array(confusionTable),
#                       normalize    = True,
#                       target_names = table2c1,
#                       title        = "Confusion Matrix")
#============

print("\n")
print("General Accuracy")
print(myAccuracy)
print("\n")

print("Accuracy per Class")
print(table2c1)
print(table2c2)
print("\n")

print("Kappa")
print(myKappa)
print("\n")

print("Performance Information")
print(table3c1)
print(table3c2)
print("\n")
