'''

    module
    
    this module is supposed to be a collection of functions that i use to do file operations within the feedLove project


'''

# libraries and classes to include
from pathlib import Path
import os
import shutil


def testPrint (str):
    return print (str)


def getFiles (path = ".", ext = "", recur = True):
# get the list of files that are of interest to me in a directory
# these are defined by
# path: files in a given path
# ext: files with an extension in a given list
# recur: true/false whether to look at subdirectories
    return os.listdir(path)


def moveFiles (files = [], fromDir = ".", toDir = "."):
# copy a list of files from one dir to another
    for fileName in files:
        srcFileName = os.path.join(fromDir, fileName)
        destFileName = os.path.join(toDir, fileName)
        print("moving " + srcFileName + " to " + destFileName)
        if (os.path.isfile(srcFileName)):
            shutil.move(srcFileName, destFileName)
    return True

