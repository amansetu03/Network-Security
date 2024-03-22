from lightphe import LightPHE
import datetime

def RSAEncryption(message):
    cs = LightPHE(algorithm_name = 'RSA')
    # define plaintexts
    m1 = 17
    # m2 = 23
    # time=datetime.datetime.now()

    # calculate ciphertexts
    c1 = cs.encrypt(m1)
    # c2 = cs.encrypt(m2)
    print(c1)
    return c1
    # print(c2)
    # performing homomorphic multiplication on ciphertexts
    # assert cs.decrypt(c1 * c2) == m1 * m2
    # d=cs.decrypt(c1*c2)
    # print("product of ciphertext",+d)

    # print("Product of plaintext",+ m1*m2)
    
    # print(datetime.datetime.now()-time)

