#from Algorithm.caesarCipher import CaesarEcrypt
from Algorithm.pallierrun import pellierrEncryption
from Algorithm.RSArun import RSAEncryption

def encryptionProsess(message,encryptionType):
    if encryptionType == "paillier":
        return pellierrEncryption(message)
    elif encryptionType == 'RSA':
        return RSAEncryption(message)
    return message