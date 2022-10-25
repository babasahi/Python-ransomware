from cryptography.fernet import Fernet


class EncryptFile:
    def encrypt(self, files):
        encryptionKey = Fernet.generate_key()
        keyHandler = open("key.txt", "wb")
        keyHandler.write(encryptionKey)
        for file in files:
            writeHandler = open((file), "wb")
            readHandler = open((file), "rb")
            file = readHandler.read()
            print("Wrote encryption key to 'key.txt' file")
            fernet = Fernet(encryptionKey)
            encrypted = fernet.encrypt(file)
            writeHandler.write(encrypted)
            print("Encryption done")
