#Jacob Amrine 8/11/21
#Moves all files within a job folder to a folder called "SoCal Y Drive" within the same folder
#For example, all files in /2019 Bids/1156 Job Example Name/* would be moved into /2019 Bids/1156 Job Example Name/SoCal Y Drive
#
#--Known Issues--
#Will error out if the file name is too long or has a weird character. If it does, move the files manually into "SoCal Y Drive" because the program will skip that folder by design

import os
import shutil
import builtins

#Specify directory you want it to work in below. Doesnt play well with the python file in the directory and I'm too lazy to fix that.
#Use two backslashes for each directory (since backslash is an escape character) Example: Y:\\BIDS So Cal\\BID FILES\\2019 Bids
currentDir = "Y:\\BIDS So Cal\\BID FILES\\2021 Bids" 
for filename in os.listdir(currentDir): #Loops through current working directory (cwd)
    if (os.path.exists(currentDir + "\\" + filename + "\\SoCal Y Drive\\")):
        #Do nothing, fall through loop
        print((currentDir + "\\" + filename + "\\SoCal Y Drive\\") + "Already exists! Doing nothing\n")
    else:
        os.mkdir(currentDir + "\\" + filename + "\\SoCal Y Drive\\")
        filenames = os.listdir(os.path.join(currentDir, filename))
        for files in filenames:
            shutil.move((currentDir + "\\" + filename + "\\" + files), (currentDir + "\\" + filename + "\\SoCal Y Drive\\"))
        print("Done moving " + filename + "\n")
print("Program terminated successfully")

                           
