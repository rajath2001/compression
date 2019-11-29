import os
from trees import *

def every_file_de(filename):
    # to go to every file if a file encode it
    if(os.path.isfile(filename)):
        if filename.endswith('.copy'):
            # print filename
            extract_dec(filename)
    else:
     os.chdir(filename)
     if(os.listdir(os.getcwd())):
        files= os.listdir(os.getcwd())
        # print files
        for i in files:
            every_file_de(filename+"/"+i)

def extract_dec(filename):
    #os.chdir(filename)
    file = open(filename,"r")
    file = file.read()
    array1 = bytearray(file) 
    # print array1
    arr=[i for i in array1]
    # print arr
    string=""
    for i in arr:
      string+="{0:0=8b}".format(i)
    filename = filename[:-5:]
    f2 = open(filename + ".keys","r")
    x = f2.read().split(",")[:-1:]
    list = [(int(x[i]),x[i+1]) for i in range(0,len(x),2) ]
    # print list
    print decode(string,list)

def decode(code,list):
   count = 0
   stri  = ""
   for i in code:
       count += 1
       stri  += i
       if(count == 8):
        x = int(stri,base = 2)
        code = code[8:-x:]
        # print code
        break
 
   decoding = ""
   codetree = fulltree=maketree(list)
   for i in code:
       if(i == "0"):
           codetree=codetree[1]   
       else:
           codetree=codetree[2]

       if(len(codetree) == 1):
           weight , char = codetree[0]
           decoding += char
           codetree = fulltree
   return decoding
