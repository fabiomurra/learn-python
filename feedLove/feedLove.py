'''
	main

    The objective of this project is to run a AI image recognition API to test it - and maybe optimise it - for the food project

    I start by writing this as a script, but I will extend it to be a more modular MVC framework 
'''

print('*** feed Love ***'),

AM_I_TESTING = True

### IMPORT ###
print('import the relevant modules \n')
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
imagesToProcess = myFileOps.getFiles("watch")

print('I have been looking for files in the watch directory. \nThis is what i found:')
print(*imagesToProcess, sep = "\n") 

# ...............
# a better way to describe the name of the image file to annotate
# file_name = os.path.join(os.path.dirname(__file__),'resources/wakeupcat.jpg')
# ...............

### SETUP ###
# as part of this project i'm using Google Vision API and i need to set myself up in order to use it
# do i need to set this up all the time?
# print('setting up the environment to run Google Vision API \n')
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = myGoogleOps.GOOGLE_APPLICATION_CREDENTIALS




### ANALYSIS ###
# set up annotator client in 'vision'
# >>> client = vision.ImageAnnotatorClient()

# load an image into your workspace
# will eventually run through the array and do this one at the time
with io.open(imagesToProcess[0], 'rb') as imageFile:
        localImageToAnalyse = imageFile.read()

# instantiate a vision object of type image
objectImageToAnalyse = vision.types.Image(content=localImageToAnalyse)

print(objectImageToAnalyse)

if (AM_I_TESTING):
    exit(0)


# analyse the image
# LABELS
response = client.label_detection(image=objectImageToAnalyse)
labels = response.label_annotations

print('Labels:')

for label in labels:
    print(label.description + "     score:" + str(round(label.score*100,1)) + "%")


print('\ndone!')