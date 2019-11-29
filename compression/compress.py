import os
from trees import *
from padding import *

def every_file(filename):
    # to go to every file if a file encode it
    if(os.path.isfile(filename)):
            encode(filename) 
    else:
     os.chdir(filename)
     if(os.listdir(os.getcwd())):
        files= os.listdir(os.getcwd())
        for i in files:
            every_file(filename+"/"+i)

def encode(filename):

  file=open(filename,"r")
  text=file.read()

# creating a dictionary to keep the frequency count
  dict={}
  for char in text:  
    if char not in dict:
        dict[char] = 1
    else:
        dict[char] += 1

# to use heapify we need a list
#converting the dict to list
  list=[]
  for dict_value in dict:
    list.append((dict[dict_value],dict_value))


  heap  = maketree(list)
  freq  = codemap(heap)
#   print(freq)
  file2 = open(filename + ".copy","w+b")
  string = ""
  count = 0
  for j in text:
    string += freq[j]
  string   = padding(string)
#   print string
  count1   = 0
  temp_str = ""
  array1 = bytearray() 
  
  for i in string:
      temp_str += i
      count1   += 1
      if count1%8 == 0:
        #   print(temp_str)
          array1.append(int(temp_str,base=2))
        #   print (int(temp_str,base=2))
        #   print array1
          temp_str=""
  file2.write(array1)
  str_final = ""
  for i in list:
      str_final+=str(i[0])+","+str(i[1])+","
  file2 = open(filename + ".keys","w")
  file2.write(str_final)

  file2.close()