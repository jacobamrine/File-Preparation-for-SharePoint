#Jacob Amrine 8/11/21
#Simple program used to remove the prepended 'E' in every folder name on the SoCal drive
#os.rename() is case sensitive, it doesnt remove all E's in the file name.

import os
for filename in os.listdir(os.getcwd()): #Loops through current working directory (cwd)
    os.rename(filename, filename.replace('E', '')) #Replaces 'E' with '' (nothing)
