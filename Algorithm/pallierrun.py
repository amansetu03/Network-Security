from lightphe import LightPHE
import datetime
# supported algorithms
algorithms = [
  'RSA',
  'ElGamal',
  'Exponential-ElGamal',
  'Paillier',
  'Damgard-Jurik',
  'Okamoto-Uchiyama',
  'Benaloh',
  'Naccache-Stern',
  'Goldwasser-Micali',
  'EllipticCurve-ElGamal'
]
 
# build a pallier cryptosystem which is homomorphic
# with respect to the addition
def pellierrEncryption(textList):
  cs = LightPHE(algorithm_name = 'Paillier')
  
  # define plaintexts
  m1 = int(textList)

  time=datetime.datetime.now()
  # calculate ciphertexts
  c1 = cs.encrypt(m1)
  # c2 = cs.encrypt(m2)

  print("C1: ")
  print(c1)
  return c1
  # print("C2: ")
  # print(c2)
  # # performing homomorphic multiplication on ciphertexts
  # assert cs.decrypt(c1 + c2) == m1 + m2
  # d=cs.decrypt(c1+c2)
  # print("sum of ciphertext",+d)

  # print("sum of plaintext",+ m1+m2)
  
  # print(datetime.datetime.now()- time)



