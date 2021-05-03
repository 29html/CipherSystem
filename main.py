from EncryptionTools import EncryptionTools

# 1. Generamos una instancia de EncryptionTools para llamar los metodos de encriptar y desencriptar
# 2. Llamamos el metodo encrypt() para encriptar el mensaje del archivo file_with_text_to_encrypt.txt y escribirlo en el archivo encrypt_result_file.txt
# 3. Llamamos al metodos decrypt() para desencriptar el mensaje encriptado del archivo encrypt_result_file.txt y escribirlo en el archivo decrypt_result_file.txt
ETs = EncryptionTools()
ETs.encrypt()
ETs.decrypt()
