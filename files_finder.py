import os

import os


def getFiles():

    supportedExtensions = ("txt", "java", "c",
                           "csv", "cgi", "pl", "html", "js", "php")
    directoryFiles = os.listdir()
    exceptions = ["py", "git", ]
    filesToEncrypt = []
    for file in directoryFiles:
        try:
            fileExtension = (str(file.rsplit(".")[1]))
        except:
            fileExtension = ""
        if (supportedExtensions.count(fileExtension) > 0) & (fileExtension != ".py"):
            filesToEncrypt.append(file)

    return directoryFiles
