'''

    module
    
    this module is supposed to be a collection of functions that i use to do file operations within the feedLove project


'''

# libraries and classes to include
from pathlib import Path
import os
import shutil
import json

# testPrint #
def testPrint (str):
    return print (str)

# checkDirExists #
# check if a directory exists
# if it doesnt create one (if create = True)
def checkDirExists (folder = "newDir", create = False):
    if (os.path.isdir(folder)):
        return True
    elif create:
        try:  
            os.mkdir(folder)
        except OSError:  
            print ("Creation of the directory %s failed" % folder)
            return False
        else:  
            print ("Successfully created the directory %s " % folder)
            return True
    else:
        print ("Directory %s does not exist and was not created" % folder)
        return False
    
# getFiles #
# get the list of files that are of interest to me in a directory
# these are defined by
# path: files in a given path
# ext: files with an extension in a given list
# recur: true/false whether to look at subdirectories (NOT YET INCLUDED/WORKING)
def getFiles (path = ".", ext = "", recur = False):
    fileList = os.listdir(path)
    fileReturnList = []
    for fileName in fileList:
        print('checking if ' + fileName + ' ends in {0} '.format(ext))
        print(fileName.lower().endswith(ext))
        if fileName.lower().endswith(ext):
            fileReturnList.append(fileName)
    return fileReturnList

# moveFiles #
# copy a list of files from one dir to another
def moveFiles (files = [], fromDir = ".", toDir = "."):
    for fileName in files:
        srcFileName = os.path.join(fromDir, fileName)
        destFileName = os.path.join(toDir, fileName)
        print("moving " + srcFileName + " to " + destFileName)
        if (os.path.isfile(srcFileName)):
            shutil.move(srcFileName, destFileName)
    return True

# dumpToKJSON #
# dump to a JSON file the content of the list
def dumpToJSON(list = [], filename = "default"):
    filename = filename + '.json'
    print("dumping list to %s " % filename)
    with open(filename, 'w') as fp:
        json.dump(list, fp)
    return True

