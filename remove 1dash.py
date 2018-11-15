import os
from pathlib import Path

'''
    This script uses os lib methods to traverse a directory tree and do the following:
    - check each file and see if another file exists with same name but prepended with a string.  In this case, the string is "1-".
     
    I created this because of MusicBee music software for pc creating duplicates when I sync/transferred music to my sony nw-a45 hd music player because I 
      hadn't set up settings in MusicBee correctly.  

    This script could be easily modified to find duplicate files using other search criteria.
'''

def getAllFilesInTree(directoryName):
    # Get the list of duplicate files (based on a specified string) in directory tree
    entriesInCurrentDir = os.listdir(directoryName)
    allFiles = list()
    # Iterate over all the entries
    for entry in entriesInCurrentDir:
        # Create full path
        fullPath = os.path.join(directoryName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getAllFilesInTree(fullPath)
        else:
            fileName = entry  # just for naming convenience, use a new var.  Assuming if it is NOT a dir than it's a file.
            if (fileName[0:2]=='1-'):   # <--- this is the string to check for
                my_file = Path(os.path.join(directoryName, fileName[2:]))
                if my_file.is_file():
                    allFiles.append(fullPath)
                
    return allFiles        


def main():
    
    startingDirectory = '.';
    
    # Get the list of duplicate files (based on a specified string) in directory tree at given path
    allFiles = getAllFilesInTree(startingDirectory)

    # Print (and remove) the duplicate files
    for fileName in allFiles:
        print("removing {}".format(fileName))
        #os.remove(fileName) # <--- uncomment this line to actually remove each duplicate file
        
if __name__ == '__main__':
    main()