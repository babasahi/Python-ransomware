from cryptography.fernet import Fernet


class EncryptFile:
    def encrypt(self, files):
        encryptionKey = Fernet.generate_key()
        keyHandler = open("key.txt", "wb")
        keyHandler.write(encryptionKey)
        print("Wrote encryption key to 'key.txt' file")
        for file in files:
            writeHandler = open((file), "wb")
            readHandler = open((file), "rb")
            file = readHandler.read()
            encrypted = Fernet(encryptionKey).encrypt(file)
            writeHandler.write(encrypted)
        print("Encryption done.")
