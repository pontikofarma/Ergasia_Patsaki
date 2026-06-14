from sage.all import *
import random
import math
import time
import base64
#from p_tqdm import p_map
start=time.time()
with open("/home/meow/patsakis_directory/chris_coding/gimp.bmp","rb")as file:
  bint=file.read()

bint=bint.hex()

breakpoint()
#image = "01010010110110101010"
interedbytes=int(bint,16)
#μετα τα κανω binary
binariedbytes=bin(interedbytes)[2:]#να θυμαμαι να βγαζω το prefix
image=str(binariedbytes)
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

def encode(c):
  c=[item[0] for item in c]# παιρνω το πρωτο αντικειμενο του tuple
  print(c) # πολλαπλασιαζμός μηνύματος(c) με generator matrix
  c=list(map(int,c))
  print(c)
 # breakpoint()               
  return vector(M, c) * G

def error_syndrome(r):        # πολλαπλασιαμός με πίνακα ελέγχου. r = c + e(error)
  return H * vector(M, r)#blammeno indent

# 128/16 = 8 σύμπλοκα

def build_error_syndrome_table():
 # M = GF(2)
  table = {}
  zero = vector(M, [0,0,0,0,0,0,0])
  table[tuple(error_syndrome(zero))] = zero # no error
  for i in range(7):
    e = [0,0,0,0,0,0,0]
    e[i] =  1
    e = vector(M, e)
    table[tuple(error_syndrome(e))] = e
  return table    

error_syndrome_table = build_error_syndrome_table()


def decode(r):
  print(r)
 # breakpoint()
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
    num_errors =  math.floor(n * error_percent) # στρογγυλοποίηση προς τα κάτω -  θα βάλει 0 ως 7 μοναδικά σφάλματα(error_percent 0-1)# οι στρογγυλοποιησεις δεν θα γινονται ετσι
    print(num_errors)
  #  breakpoint()
    error_positions = random.sample(range(n), min(num_errors, n)) # βρίσκει τις θέσεις στις οποίες θα βάλει τα σφάλματα
    
    for pos in error_positions:
         codeword[pos] = int(codeword[pos]) ^ 1   # στις θέσεις που υπολόγισε αλλάζει τα bits
         return codeword

def xor_lists(a,b):
  r=[(i+j)%2 for i,j in zip(a,b)]
  return r
def add_noise(l,p): #πατσακο συναρτηση για σφαλμα
  e=[]
  for i in range(len(l)):
    r=random.randrange(100)
    if r<p:
      e.append(1)
    else:
      e.append(0)
  return xor_lists(e,l)
output_ls=[]

def manosdef(chunk):
    bits = [tuple(b) for b in chunk]
    codeword = encode(bits) # 
    print(codeword)
   # breakpoint()
    received = add_noise(list(codeword), 5)
    print(received)
  #  breakpoint()
    return decode(received)
#for i, chunk in enumerate(chunks):
 #   bits = [tuple(b) for b in chunk]
  #  codeword = encode(bits) # 
  # print(codeword)
   # breakpoint()
   # received = add_noise(list(codeword), 5)
    #print(received)
  #  breakpoint()
    #output_ls.append(decode(received))

output_ls=list(map(manosdef,chunks))
def appender(lista):
  stringu=""
  for item in lista:
    stringu+=str(item)
    return stringu
print(image)
final_stirng=""
print(output_ls)
final_ls=[]
def list_returner(item):
  #print(item[0])
  if item[0]==0 or item[0]==1:
    return item[1]
  if item[1]==0 or item[1]==1:
    return item[0]
  
  return item[0]+item[1]
demo_ls=[]
if 0 in output_ls:
  output_ls=[item for item in output_ls if item!=0]
def koftis_liston(output_ls):
  n=len(output_ls)
  if n%2==0:
    flag=0
    lista1=output_ls[:int(n/2)]
    lista2=output_ls[int(n/2):]
  else:
    flag=1
    teleutaio=output_ls.pop()
    #breakpoint()
    #if teleutaio==0:
    #  print("bomb")
    #  exit()
    lista1=output_ls[:int(n/2)]#καπου δημιουργειται ενα μηδενικο εδψ και μου τα χαλαει ολα γαμωωω
    lista2=output_ls[int(n/2):]

  teliki_lista=list(map(list_returner,zip(lista1,lista2)))
  if flag==1:
    try:
      teliki_lista+=teleutaio
    except:
      print("whoops")
  
  print(type(teliki_lista))
  print(teliki_lista)
  #breakpoint()
  return teliki_lista
#breakpoint()#απο ποθ γεννιουνται τα μηδενικα :(((((((((((((())))))))))))))

#breakpoint()
#while(len(output_ls)!=1):
 # for i in range(0,len(output_ls)-1,2):
  #  demo_ls.append(list_returner(output_ls[i],output_ls[i+1]))
  #output_ls=demo_ls
  #print(len(output_ls))

 
  
#print(final_ls)
#image_output=""
final_ls=[]
for item in output_ls:
  final_ls.extend(item)
  print("a")

strfinal_ls=map(str,final_ls)
teliko_string="".join(strfinal_ls)# is this too much voodo ?? 
#teliko_string="".join(final_ls)
#print(image_output==image)# το θεμα μας ειναι πως δεν βγαινουν ολα true 
end=time.time()
breakpoint()
bits_to_bytes=bytes(int(teliko_string[i:i+8],2)for i in range(0,len(teliko_string),8))
breakpoint()
print("ntinos")
with open("outputer.bmp","wb")as file:
  file.write(bits_to_bytes)
codeword = ''.join(str(byte) for byte in codeword)
codeword = bytes(int(codeword[i:i+8], 2) for i in range(0, len(codeword), 8))
codeword = base64.b64encode(codeword).decode("utf-8")


decoded = base64.b64decode(codeword)  
decoded = ''.join(f'{byte:08b}' for byte in decoded)
result = decode(received)

#=int(image_output)
#f = open("photo.bmp" ,"wb") 
#f.write(bits_to_bytes)
#f.close()