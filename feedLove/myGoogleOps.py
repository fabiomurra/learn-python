
'''

    module
    
    this module is a collection of a whole bunch of operations that i need to drive the Google APIs

    included to date:
    - Google Vision API


'''

### IMPORT all relevant modules ###
import os
from google.cloud import vision
from google.cloud.vision import types


### VARIABLES ###

# GCP: Vision API JSON file (not included as part of the Git Commit, ie local only, as it contains keys information)
GCP_JSON_FILEPATH = 'C:\\Users\\fabio.murra\\source\\repos\\learn-python\\feedLove\\keys\\'
GCP_JSON_FILE = 'feedlove01-65c771c48b27.json'
# GCP: Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the file path of the JSON file that contains your service account key. 
# GCP: https://cloud.google.com/vision/docs/quickstart-client-libraries#client-libraries-install-python
GOOGLE_APPLICATION_CREDENTIALS = GCP_JSON_FILEPATH + GCP_JSON_FILE
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

print("GOOGLE_APPLICATION_CREDENTIALS is set to " + os.environ["GOOGLE_APPLICATION_CREDENTIALS"])


### CLIENT ###

# setup a Google Vision Client 
# this will be needed for all operations
# should it be included inside the various functions?
#GVClient = vision.ImageAnnotatorClient()
