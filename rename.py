#Jacob Amrine 8/11/21
#This program looks at the first 6 characters in a folder name, then matches it with a name from names.csv
#Used on the SoCal Y Drive to match the job names
#Once the job names were matched the migration tool could be used to "merge" the folders in SharePoint

import os
import csv
import sys

for filename in os.listdir(os.getcwd()): #Loops through current working directory (cwd)
    jobNum = filename[0:5]
    file = csv.reader(open('names.csv', "r"), delimiter=",")
    for row in file:
        rowname = row[0] #Holds the name of the row
        if jobNum == rowname[0:5]: #If first 6 characters match
            os.rename(filename, rowname) #Rename the folder to the row name in the csv file
