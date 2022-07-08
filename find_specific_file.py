
# Finding specific files on your system

import fnmatch 
import os

rootPath = '/'

def searchFiles():
    pattern = input("Enter pattern of file i.e:*.mp3: ")

    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print(os.path.join(root, filename))

print(searchFiles())
