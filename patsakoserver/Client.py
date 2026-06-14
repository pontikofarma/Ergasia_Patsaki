import json
import os
from PIL import Image
import hashlib
import requests

import subprocess
import sumpiesh


headers = {'Content-type': 'application/json'}

param_list=[]
info={  
"encoded_image": "",
"compression_algorithm": "arithmetic",
"encoding": "linear",
"parameters":[param_list],
"errors": "",
"SHA256": "",
"entropy":""
}


#Εδώ βάζουμε την εικόνα που θέλουμε να χρησιμοποιήσουμε
print("Enter the image name:")
imagefile=input()
isimage=False

#imagefile='zouzouni.png'

#παράδειγμα αρχείου που δεν είναι εικόνα για είσοδο
#imagefile='NotAnImage.txt'



def is_valid_image_pillow(imagefile):
    
    while isimage==False:
        
        try:
            with Image.open(imagefile) as img:

                img.verify()
                isimage==True
                print("Image is valid")
                break

        except (IOError, SyntaxError):
                
                isimage==False
                print("Not an image!Enter the correct file type")
                imagefile=input()
    return imagefile
   

imagefile=is_valid_image_pillow(imagefile)

#---Εικόνα---

subprocess.call(['python', 'sumpiesh\map_wencode.py'])

f = open('sumpiesh\\tag_ls2','rb')
bin = f.read()
f.close()
hex_bin=bin.hex()

#ανοίγω και διαβάζω την εικόνα, την μετατρέπω σε 16ικο και τη βάζω στο dictionary
'''
f = open(imagefile,'rb')
bin = f.read()
f.close()
hex_bin=bin.hex()
'''

info["encoded_image"]= hex_bin

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


#---Errors---
print("Errors (0-100):")
info["errors"]=input()
print(info["errors"])


#---SHA256---
hash_object = hashlib.sha256(hex_bin.encode())
hex_digest = hash_object.hexdigest()
info["SHA256"]=hex_digest
print(f"SHA256:{hex_digest}")


#---Εντροπία---
with Image.open(imagefile) as im:

    info["entropy"]=im.entropy()

print(f"Entropy:{info['entropy']}")


#βάζω τα στοιχεία του dictionary σε ενα καινούριο json
("info.json", {})

with open("info.json", "w") as f:
        json.dump(info, f, indent=4)

#print(info["compression_algorithm"])


response = requests.post(url="http://192.168.2.8:5000/", json=info , headers=headers)

print(response.text)

