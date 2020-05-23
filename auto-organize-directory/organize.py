import os;

# Dictionary: Organizing directory
# KEY:VALUE
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

## Pluck out a particular type of files
def pickDirectory(value):
    for key,val in SUBDIRECTORIES.items():
        for values in val:
            if values == value:
                return key;
    return 'MISC';

print(pickDirectory('.pdf'));
    

## Organize the different files into separate directories
def organizeDirectory():
    
    for items in os.scandir(): # Lets you loop through all the files in the directory
        # Skip if the item is a directory
        if items.is_dir():
            continue

        filePath = os.path(items); # We have the path of each item in the directory
        fileType = filePath.suffix.lower(); # Gets the extension
        directory = pickDirectory(fileType); 
        directoryPath = os.path(directory); # Gets the path of each of the directory

        if directoryPath.is_dir() != True:
            directoryPath.mkdir(); # Make a new directory if not available

        # Moving the files into new directories
        filePath.rename(directoryPath.joinpath(filePath));


organizeDirectory();