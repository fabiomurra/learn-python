'''
	this script is being developed to go and look through all video files in a given path and convert them using FFMPEG to a common mezzanine format that is most compatible with all of the entertainment systems in the house
'''
# some variables
videoPath = "\\\pippo3\\video\\Kids"							# the path where I'm looking to convert videos
videoExtensionsSupported = [".ts", ".mp4", ".mkv", ".mov"]		# the videos extensions supported
videosInPath = []												# this will be the list of videos I found in path

# libraries and classes to include
from pathlib import Path

# list the content of the current directory
for videoFile in Path(videoPath).iterdir():
	#	print(videoFile.suffix)
	if videoFile.suffix in videoExtensionsSupported:
		print(videoFile.suffix)
		videosInPath.append(videoFile)

print("I found ", len(videosInPath), " supported videos")
print(videosInPath)


# returns the content of the current directory in a list
# as elements WindowsPath
# https://docs.python.org/3/library/pathlib.html
contents = list(Path(videoPath).iterdir())
