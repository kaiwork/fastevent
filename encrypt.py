import pyAesCrypt
import bcrypt
import os
cwd = os.getcwd()

password = "==="
salt = '===='.encode(
    'utf-8')
hashed_password = bcrypt.hashpw(
    password.encode('utf-8'), salt)
hashed_password = hashed_password.decode('utf-8')
print(hashed_password)

encrypted_file_path = "{}/credentials/credentials.json.aes".format(cwd)
decrypted_file_path = "{}/credentials/credentials.json".format(cwd)
print(encrypted_file_path)
print(decrypted_file_path)
# encrypt
pyAesCrypt.encryptFile(decrypted_file_path,
                       encrypted_file_path, hashed_password)
# decrypt
pyAesCrypt.decryptFile(encrypted_file_path,
                       decrypted_file_path, hashed_password)