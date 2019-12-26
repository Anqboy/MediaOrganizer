import os
import platform
import shutil
from datetime import datetime

MediaFileSuffix = (
    "JPG",
    "PNG",
    "MOV",
    "HEIC",
    "AAE",
    "MP4"
)

DateFormat = "%Y-%m" #2019-11

def getModifiedDatetime(file, format = None):
    timestamp = os.path.getmtime(file)
    dt = datetime.fromtimestamp(timestamp)
    if format:
        return dt.strftime(format)
    else:
        return dt

def sortIntoFolders(replace = False):
    for item in os.listdir():
        if not os.path.isfile(item):
            continue
        
        suffix = item.split('.')[-1].upper()
        if suffix not in MediaFileSuffix:
            continue
        
        modifiedDate = getModifiedDatetime(item, DateFormat)

        if not os.path.exists(modifiedDate):
            os.mkdir(modifiedDate) 

        destination = modifiedDate + "/" + item

        if not os.path.isfile(destination) or replace:
            shutil.move(item, modifiedDate + "/" + item)

if __name__ == "__main__":      
    sortIntoFolders()

