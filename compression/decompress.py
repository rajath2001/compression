import os
from trees import *

def every_file_de(filename):
    # to go to every file if a file encode it
    if(os.path.isfile(filename)):
        if filename.endswith('.copy'):
            # print filename
            extract_dec(filename)
        if filename.endswith('.keys'):
            os.remove(filename)
            
    else:
     os.chdir(filename)
     if(os.listdir(os.getcwd())):
        files= os.listdir(os.getcwd())
        # print files
        for i in files:
            every_file_de(filename+"/"+i)

def extract_dec(filename):
    #os.chdir(filename)
    filename2 = filename[:-5:]
    file = open(filename,"r")
    file = file.read()
    os.remove(filename) 
    array1 = bytearray(file) 
    # print array1
    arr=[i for i in array1]
    # print arr
    string=""
    for i in arr:
      string+="{0:0=8b}".format(i)
    filename = filename[:-5:]
    f2 = open(filename + ".keys","r")
    # x = f2.read().split(",")[:-1:]
    x = f2.read().split(",")
    y = []
    count = 0
    for i in range(0,len(x)-1):
        if(x[i] == '' and x[i+1] == ''):
            print "hii"
            y.append(",")
            count+=1
        else:
            if(count==1):
                count += 1
            else:
                y.append(x[i])
    
    print y
    list = [(int(y[i]),y[i+1]) for i in range(0,len(y),2) ]
    # print list
    message = decode(string,list)
    file_org = open(filename2 , "w")
    file_org.write(message)

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
