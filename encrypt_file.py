from cryptography.fernet import Fernet


class EncryptFile:
    def encrypt(self, files):

        for file in files:
            print()
            writeHandler = open((file), "wb")
            readHandler = open((file), "rb")
            file = readHandler.read()
            encryptionKey = Fernet.generate_key()
            keyHandler = open("key.txt", "wb")
            keyHandler.write(encryptionKey)
            print("Wrote encryption key to 'key.txt' file")
            fernet = Fernet(encryptionKey)
            encrypted = fernet.encrypt(file)
            writeHandler.write(encrypted)
            print("Encryption done")
