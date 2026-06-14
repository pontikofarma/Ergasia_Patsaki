from sage.all import *
import random
import base64
import hashlib

image = ""

while len(image) % 4 != 0:     # padding
          image += "0"

chunks = [image[i:i+4] for i in range(0, len(image), 4)]   # split into chunks of 4
          
M = GF(2)

# 16 διαφορετικά μηνύματα(2^4)
# 128 διαφορετικοί vectors(2^7)

G = matrix(M, [                # generator matrix απο το βιβλιιο (7,4)
          [1,0,0,0,1,1,1],
          [0,1,0,0,1,1,0],
          [0,0,1,0,1,0,1],
          [0,0,0,1,0,1,1]
          ])           

H =  matrix(M, [              # πίνακας ελέγχου από το βιβλίο (7,3)
            [1,1,1,0,1,0,0],
            [1,1,0,1,0,1,0],
            [1,0,1,1,0,0,1]
            ])

# Κάθε vector() ή tuple() αλλάζει τον τύπο τις μεταβλητής όπως χρειάζεται για να μπορέσουν να γίνουν οι πράξεις

def encode(c):                # πολλαπλασιαζμός μηνύματος(c) με generator matrix
  return vector(M, c) * G

def error_syndrome(r):        # πολλαπλασιαμός με πίνακα ελέγχου. r = c + e(error)
   return H * vector(M, r)

# 128/16 = 8 σύμπλοκα

def build_error_syndrome_table():
  table = {}
  zero = vector(M, [0,0,0,0,0,0,0])
  table[tuple(error_syndrome(zero))] = zero # no error
  for i in range(7):
    e = [0,0,0,0,0,0,0]
    e[i] =  1
    e = vector(Μ, e)
    table[tuple(error_syndrome(e))] = e
  return table    

error_syndrome_table = build_error_syndrome_table()


def decode(r):
  r = vector(M, r)
  s = tuple(error_syndrome(r))
  if all (v == 0 for v in s):          # αν = 000 σημάινει οτι δεν έχει σφάλματα
    print("No errors")
    corrected = r
  elif s in error_syndrome_table:
    corrected = r - error_syndrome_table[s]  # XOR
  else:
    print("More than 1 errors. Can't be corrected")
    return None

  message = list(corrected)[:4]          # Παίρνουμε τα πρώτα 4 bits που είναι = αρχικό μήνυμα
  print(f"Decoded message: {message}")
  return message



def add_errors(codeword, error_percent):

    codeword = list(codeword)
    n = len(codeword)    # πάντα 7 
    num_errors =  int(n * error_percent))  # στρογγυλοποίηση προς τα κάτω -  θα βάλει 0 ως 7 μοναδικά σφάλματα(error_percent 0-1)
    
    error_positions = random.sample(range(n), min(num_errors, n)) # βρίσκει τις θέσεις στις οποίες θα βάλει τα σφάλματα
    
    for pos in error_positions:
         codeword[pos] = int(codeword[pos]) ^ 1   # στις θέσεις που υπολόγισε αλλάζει τα bits
         return codeword

def do_SHA256(codeword):
          b = ''.join(str(i) for i in codeword)
          b2 = b.encode("utf-8")
          return hashlib.sha256(b2).hexdigest()


for i, chunk in enumerate(chunks):
    bits = [tuple(b) for b in chunk]
    codeword = encode(bits)
    #base64
    codeword2 = ''.join(str(byte) for byte in codeword)
    codeword2 = bytes(int(codeword2[i:i+8], 2) for i in range(0, len(codeword2), 8))
    codeword64 = base64.b64encode(codeword2).decode("utf-8")
    #SHA256
    h = do_SHA256(codeword)
          
    received = add_errors(codeword, error_percent=0.10)
    decode(received)
