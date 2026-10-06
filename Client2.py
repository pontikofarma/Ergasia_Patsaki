import json
import os
import hashlib
import requests
import math 
import subprocess
import string
import sys
#import sumpiesh


headers = {'Content-type': 'application/json'}

param_list=[]
info={  
"encoded_file": "",
"compression_algorithm": "arithmetic",
"encoding": "linear",
"parameters":[param_list],
"errors": "",
"SHA256": "",
"entropy":""
}


#Εδώ βάζουμε το όνομα του αρχείου που θέλουμε να χρησιμοποιήσουμε
print("Enter the text file name:")
txtfile=input()


#---Εικόνα---
'''
subprocess.call(['python', 'sumpiesh\\map_wencode.py'])

f = open('sumpiesh\\tag_ls2','rb')
bin = f.read()
f.close()
hex_bin=bin.hex()
'''

#ανοίγω και διαβάζω την εικόνα, την μετατρέπω σε 16ικο και τη βάζω στο dictionary

with open(txtfile, 'r') as file:
    file_content = file.read()

'''
file = open(txtfile,'r')
bin = file.read()
file.close()
#hex_bin=bin.hex()

lines =words = chars = spaces = 0

with open(file, "r") as f:
    for x in f:
        lines += 1
        words += len(x.split())
        spaces += x.count(" ")
        chars += sum(1 for c in x if c not in (" ", "\n"))

print("Lines:", lines)
print("Words:", words)
print("Characters:", chars)
print("Spaces:", spaces)

entropy = 0
for x in range(chars):
    p_x = float(data.count(chr(x)))/len(data)
    if p_x > 0:
      entropy += - p_x*math.log(p_x, 2)
print(entropy)
'''


#info["encoded_image"]= hex_bin

#---Αλγόριθμος συμπίεσης---
print(f"Compression Algorithm:{info['compression_algorithm']}")

#---Encoding---
print(f"Encoding:{info['encoding']}")

#---Λίστα παραμέτρων---
'''
print("Enter the parameters")
text=input()
while (text!="end"):
    
    if(text!="end"):
        param_list.append(text)
    text=input()
'''

#param_list.append()

'''
def arxeia(file):
    f = open(file,'rb')
    bin = f.read()
    f.close()
    hex_bin=bin.hex()
    param_list.append(hex_bin)

arxeia("sumpiesh\\arithmos_bit2")
arxeia("sumpiesh\\noumero2")
arxeia("sumpiesh\\diafora2")
arxeia("sumpiesh\\ls_pososta_ls2")
arxeia("sumpiesh\\ls_xarakthres_ls2")
#arxeia("sumpiesh\\arithmos_bit2")
        
#print(f"Parameter List:{param_list}")
print("parameters imported")
'''

#---Errors---
print("Errors (0-100):")
info["errors"]=input()
print(info["errors"])


#---SHA256---
hash_object = hashlib.sha256(file_content.encode())
hex_digest = hash_object.hexdigest()
info["SHA256"]=hex_digest
print(f"SHA256:{hex_digest}")


#---Εντροπία---

def entropy_finder(data):
     if not data:
          print("de douleuw pali")
          return 0
     entropy=0
     for x in string.printable:
        p_x = float(data.count(x))/len(data)
        if p_x > 0:
             entropy += - p_x*math.log(p_x, 2)
     return(entropy)   


Text_entropy= entropy_finder(file_content)     
info["entropy"]=Text_entropy
print(f"entropy:{Text_entropy}")


#βάζω τα στοιχεία του dictionary σε ενα καινούριο json
("info.json", {})

with open("info.json", "w") as f:
        json.dump(info, f, indent=4)

#print(info["compression_algorithm"])


#response = requests.post(url="http://192.168.2.8:5000/", json=info , headers=headers)
response = requests.post(url="http://127.0.0.1:5000/", json=info , headers=headers)

print(response.text)

