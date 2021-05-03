from cryptography.fernet import Fernet

class PrivateKeyTools:

    def generatePrivateKey(self):
        privateKey = Fernet.generate_key()
        with open("private.key", "wb") as keyFile:
            keyFile.write(privateKey)

    def loadKey(self):
        return open("private.key", "rb").read()


