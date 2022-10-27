import os

import os


def getFiles():
    directoryFiles = os.listdir()
    exceptions = ["py", "gitignore", "git", "md"]
    filesToEncrypt = []
    for file in directoryFiles:
        try:
            if str(file).count(".") > 0:
                fileExtension = (str(file.rsplit(".")[1]))
        except:
            fileExtension = ""
        if fileExtension != "":
            if (exceptions.count(fileExtension) < 1):
                filesToEncrypt.append(file)

    return filesToEncrypt
