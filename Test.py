#Using python library "cryptography" to create the start of a program which will encrypt a message and also creates key to open encrypted message
from cryptography.fernet import Fernet 

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key","wb") as key_file:
        key_file.write(key)
        print('key is generated')

#The key is QEqSE_AqXPISbEH6jVgRmsnfMqMFVkT3PymLRz7IERI=

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    print(encrypt_message)

encrypt_message("Python is fun") #the following message is displayed: "<function encrypt_message at 0x000001B9EDE388B0>"