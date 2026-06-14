import subprocess
from mpmath import mp,mpf
import time,sys
import pickle
#from parallel_encode import encoder
from maped_decode import decoder
import threading
from p_tqdm import p_map
import sys


arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
arg4 = sys.argv[4]
arg5 = sys.argv[5]
arg6 = sys.argv[6]

#arithmos
file_to_send=open(arg2,'rb')
arithmos_bit=pickle.load(file_to_send)
file_to_send.close()
mp.dps=2*arithmos_bit

file_to_send=open(arg1,'rb')
#tag_ls=pickle.load(file_to_send)
#file_to_send.close()

#pososta
file_to_send=open(arg5,'rb')
ls_pososta_ls=pickle.load(file_to_send)
file_to_send.close()

#xarakthres
file_to_send=open(arg6,'rb')
ls_xarakthres_ls=pickle.load(file_to_send)
file_to_send.close()

#noumero
file_to_send=open(arg3,'rb')
noumero=pickle.load(file_to_send)
file_to_send.close()

#diafora
file_to_send=open(arg4,'rb')
diafora=pickle.load(file_to_send)
file_to_send.close()
#breakpoint()
#arithmos_bit=apothikeutiki_lista2[0]
#tag_ls=apothikeutiki_lista2[1]
#ls_pososta_ls=apothikeutiki_lista2[2]
#ls_xarakthres_ls=apothikeutiki_lista2[3]
#3noumero=apothikeutiki_lista2[4]
#diafora=apothikeutiki_lista2[5]
#print(apothikeutiki_lista==apothikeutiki_lista2)
#for i in range(0,len(apothikeutiki_lista)):
 #   print(apothikeutiki_lista[i]==apothikeutiki_lista2[i])
#exit()
endno=noumero
endno-=1
noumero=0
strnoumero=str(noumero)
#breakpoint()#mfw χανονται δεκα μπιτ γαμω το σπιτι μου γαμω το σπιτι μου γιατι χανονται δεκα μπιτ

output_ls=len(tag_ls)*[""]
#b##reakpoint()
lista_dedomenon=[]
#breakpoint()
for i in range(0,len(tag_ls)):
   # print(i)
    #if i+1==len(tag_ls):
     #   lista_demo=tag_ls[i],ls_pososta_ls[i],ls_xarakthres_ls[i],arithmos_bit
      #  print("I HAPPENEEEEEEEEEEEEEEEEED")
       # break
    lista_demo=tag_ls[i],ls_pososta_ls[i],ls_xarakthres_ls[i],arithmos_bit
    lista_dedomenon.append(lista_demo)

output_ls=p_map(decoder,lista_dedomenon)

print("egina")
fin_output="".join(output_ls)
#breakpoint()
fin_output=fin_output[:len(fin_output)-(arithmos_bit-diafora)]
with open("output.bmp","wb") as file:
        file.write(bytes.fromhex(fin_output))
#end=time.time()
#print("διηρκησα",end-start," δευτερολεπτα")
#subprocess.run(['python','decode_from_file_and_append_to_final.py',strnoumero])





