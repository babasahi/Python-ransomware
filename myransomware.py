
import os
from encrypt_file import EncryptFile


encrypt = EncryptFile()

directoryFiles = os.listdir()
filesToEncrypt = []
for file in directoryFiles:
    if file.endswith(".txt"):
        filesToEncrypt.append(file)


print(filesToEncrypt)
encrypt.encrypt(filesToEncrypt)
