from cryptography.fernet import Fernet


class EncryptFile:
    def encryptLineByLine(self, files):

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
            textbytes = []
            for line in file:
                print('Line to encrypt :\n')
                print(str(line.to_bytes))
                textbytes.append(str(line).encode("ascii"))

            writeHandler.write(str(textbytes).encode("ascii"))
            print("Encryption done")

    def encryptAll(fileName):
        writeHandler = open(("encypted"+fileName+".txt"), "wb")
        readHandler = open((fileName+".txt"), "rb")
        file = readHandler.read()
        encryptionKey = Fernet.generate_key()
        keyHandler = open("key.txt", "wb")
        keyHandler.write(encryptionKey)
        print("Wrote encryption key to 'key.txt' file")
        fernet = Fernet(encryptionKey)
        encrypted = fernet.encrypt(file)
        print("Encrypted file")
        writeHandler.write(encrypted)
        print("done")
