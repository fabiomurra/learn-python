'''
	main

    The objective of this project is to run a AI image recognition API to test it - and maybe optimise it - for the food project

    I start by writing this as a script, but I will extend it to be a more modular MVC framework 
'''

print('*** feed Love ***'),

# some set variables (could become arguments)
AM_I_TESTING = True
WATCH_DIR = "watch"
PROC_DIR = "proc"
SUPPORTED_IMAGES = ['jpg', 'png']

### IMPORT ###
print('importing the relevant modules')
import os
import io
import sys
import myFileOps
import myGoogleOps
# do i need these here? i already have them in myGoogleOps
from google.cloud import vision
from google.cloud.vision import types


# IMAGES to be analysed 
# for now this is expected to be found in a WATCH folder 
# the operation returns a list
print('fetching images to be analysed')
print('supported image types are: %s' % SUPPORTED_IMAGES)
if myFileOps.checkDirExists(WATCH_DIR, True):
    imagesToProcess = myFileOps.getFiles(WATCH_DIR, False)
else:
    print("Error in fetching content from directory %s " % WATCH_DIR)
    exit(0)

# if the list is empty, there are no files to process, i will just exit
if (len(imagesToProcess)==0):
    print('There are no files to process. Exiting!')
    exit(1)

print('I have been looking for files in the %s directory. \nThis is what i found:' % WATCH_DIR)
print(*imagesToProcess, sep = "\n") 

# Run through the images in the array and process one at the time
for image in imagesToProcess:
    imageFullPath = WATCH_DIR + '/' + image
    try:     
        os.path.exists(imageFullPath)
        # get google to analyse it and return sth
        print('processing %s ' % imageFullPath)
        imageLabels = myGoogleOps.GV_getLabels(imageFullPath)
        imageLabelsList = []
        for label in imageLabels:
            imageLabelsList.append({'description': label.description, 'score': label.score, 'mid': label.mid})
        myFileOps.dumpToJSON(imageLabelsList, os.path.splitext(imageFullPath)[0])
    except OSError:    
        print ("Exeption in analysing of %s " % imageFullPath)
        

# left to do, dump output of each image to JSON (properly formatted - at the moment is not)
# copy with the same name of the image to proc (i shuold already put the json in proc - it's not to watch)
# remove the image from watch

print('\ndone!')