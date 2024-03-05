"""
A python script for validating a file path matches an expected path to prevent directory traversal
"""

import os
import ntpath
import base64

testFile = '/Users/nbrown/Dropbox/'
basedir = ntpath.split(testFile)[0]
print(basedir)

filename = ntpath.basename(testFile)

securefile = "".join(x for x in filename if (x.isalnum() or x in "._- "))
print(securefile)

fullpath = f"{basedir}/{securefile}"
fullpath = base64.urlsafe_b64encode(fullpath.encode('ascii'))

print(base64.urlsafe_b64decode(fullpath))

print(os.path.exists(base64.urlsafe_b64decode(fullpath)))

allowedPath = "/Users/nbrown/Dropbox/"

testPath = "/Users/nbrown/Dropbox/Personal Programs/../"  # Path Traversal - Bad

if os.path.commonprefix((os.path.realpath(testPath), allowedPath)) != allowedPath:
    print(f"Requested location is bad")
else:
    print(f"Path: {os.path.realpath(testPath)} is a valid path.")

    if os.path.exists(os.path.realpath(testPath)):
        print(f"Test Path: {testPath} does exist!")
        print(f"The real path is: {os.path.realpath(testPath)}")
    else:
        print("Bad Path")
        print(f"Path: {os.path.realpath(testPath)} is not valid")
