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
SUPPORTED_IMAGES = ('.jpg', '.jpeg', '.png')

### IMPORT ###
print('importing the relevant modules')
import os
import io
import sys
import ntpath
import myFileOps
import myGoogleOps
# do i need these here? i already have them in myGoogleOps
from google.cloud import vision
from google.cloud.vision import types


# IMAGES to be analysed 
# for now this is expected to be found in a WATCH folder 
# the operation returns a list
print('fetching images to be analysed')
print('supported image types are: {0}'.format(SUPPORTED_IMAGES))
if myFileOps.checkDirExists(WATCH_DIR, True):
    imagesToProcess = myFileOps.getFiles(WATCH_DIR, SUPPORTED_IMAGES, False)
else:
    print("Error in fetching content from directory %s " % WATCH_DIR)
    exit(0)
# create destination directory
myFileOps.checkDirExists(PROC_DIR, True)

# if the list is empty, there are no files to process, i will just exit
if (len(imagesToProcess)==0):
    print('There are no files to process. Exiting!')
    exit(1)

print('I have been looking for files in the %s directory. \nThis is what i found:' % WATCH_DIR)
print(*imagesToProcess, sep = "\n") 

# Run through the images in the array and process one at the time
counter = 0
for image in imagesToProcess:
    imageFullPath = os.path.join(WATCH_DIR, image)
    try:     
        os.path.exists(imageFullPath)
        # get google to analyse it and return sth
        print('processing %s ' % imageFullPath)
        imageLabels = myGoogleOps.GV_getLabels(imageFullPath)
        imageLabelsList = []
        # build a list of GC vision results with the label i want
        for label in imageLabels:
            imageLabelsList.append({'description': label.description, 'score': label.score, 'mid': label.mid})
        # dump the list to a JSON file, already in the destination directory
        myFileOps.dumpToJSON(imageLabelsList, os.path.join(PROC_DIR, os.path.splitext(ntpath.basename(imageFullPath))[0]))
        # move the image file in the destination directory as well (itd be more efficient to do it in bulk)
        myFileOps.moveFiles([image],WATCH_DIR,PROC_DIR)
        counter = counter + 1
        print ("done: [%s/%s]" % (counter, len(imagesToProcess)))
    except OSError:    
        print ("Exeption in analysing of %s " % imageFullPath)
        

# left to do, dump output of each image to JSON (properly formatted - at the moment is not)
# copy with the same name of the image to proc (i shuold already put the json in proc - it's not to watch)
# remove the image from watch

print('\ndone!')