from cryptography.fernet import Fernet

from PrivateKeyTools import PrivateKeyTools

FILE_WITH_TEXT_TO_ENCRYPTING = "Files/file_with_text_to_encrypt.txt"
ENCRYPTED_RESULT_FILE = "Files/encrypt_result_file.txt"
DECRYPTED_RESULT_FILE = "Files/decrypt_result_file.txt"


class EncryptionTools:
    def getPrivateKey(self):
        PKTs = PrivateKeyTools()
        return PKTs.loadKey()

    def encrypt(self):
        PRIVATE_KEY = self.getPrivateKey()
        f = Fernet(PRIVATE_KEY)
        with open(FILE_WITH_TEXT_TO_ENCRYPTING, "rb") as file:
            file_with_info = file.read()
        encrypted_data = f.encrypt(file_with_info)
        with open(ENCRYPTED_RESULT_FILE, "wb") as file:
            file.write(encrypted_data)

    def decrypt(self):
        PRIVATE_KEY = self.getPrivateKey()
        f = Fernet(PRIVATE_KEY)
        with open(ENCRYPTED_RESULT_FILE, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(DECRYPTED_RESULT_FILE, "wb") as file:
            file.write(decrypted_data)
