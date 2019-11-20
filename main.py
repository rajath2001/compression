import os
import heapq 
import sys
import struct

def every_file(filename):
    # to go to every file if a file encode it
    if(os.path.isfile(filename)):
       encode(filename) 
    else:
     os.chdir(filename)
     if(os.listdir(os.getcwd())):
        files= os.listdir(os.getcwd())
        print files
        for i in files:
            every_file(filename+"/"+i)
   


def padding(string):
    # adding extra zeros at make it divisible by 8 and storing that extra info
    num_zero = 8 - len(string) % 8
    for i in range(num_zero):
        string+='0'
    
    start="{0:0=8b}".format(num_zero)
    print start
    start=start+string
    return start



def walktree(heap,freq,code):
    # walkes through the tree and to find Huffman code of each character
    if(len(heap)==1):
        times,charec=heap[0]
        freq[charec]=code
    else:
        char,child1,child2=heap
        walktree(child1,freq,code+"0")
        walktree(child2,freq,code+"1")

def codemap(heap):
    freq={}
    walktree(heap,freq,"")
    return freq

def maketree(list):
    heap=[]
    for i in list:
       heapq.heappush(heap,[i])
    while (len(heap) > 1):
      child1 = heapq.heappop(heap)
      child2 = heapq.heappop(heap)
      comb_freq=child1[0][0] + child2[0][0]
      comb_char=child1[0][1] + child2[0][1]
      node=[(comb_freq,comb_char),child1,child2]
      heapq.heappush(heap,node)
    return heap.pop()

def extract_dec(filename):
    file = open(filename+"c","r")
    file = file.read()
    array1 = bytearray(file) 
    print array1
    arr=[i for i in array1]
    print arr
    string=""
    for i in arr:
      string+="{0:0=8b}".format(i)
    f2=open(filename+"k","r")
    x = f2.read().split(",")[:-1:]
    list = [(int(x[i]),x[i+1]) for i in range(0,len(x),2) ]
    print list
    print decode(string,list)

def decode(code,list):
   count=0
   stri=""
   for i in code:
       count+=1
       stri+=i
       if(count==8):
        x = int(stri,base=2)
        code=code[8:-x:]
        print code
        break
   
    


   decoding=""
   codetree=fulltree=maketree(list)
   print codetree
   for i in code:
       if(i == "0"):
           #print codetree[1]
           codetree=codetree[1]
          
       else:
           codetree=codetree[2]
       if(len(codetree)==1):
           weight,char=codetree[0]
           decoding+=char
           codetree=fulltree
   return decoding

def encode(filename):

  file=open(filename,"r")
  text=file.read()

# creating a dictionary to keep the frequency count
  dict={}
  for char in text:  
    if char not in dict:
        dict[char]=1
    else:
        dict[char]+=1

# to use heapify we need a list
#converting the dict to list
  list=[]
  for dict_value in dict:
    list.append((dict[dict_value],dict_value))
  print list

  heap = maketree(list)
  freq = codemap(heap)
  print(freq)
  array1 = bytearray() 
  file2=open(filename+"c","w+b")
  string=""
  count=0
  for j in text:
    string+=freq[j]
  string = padding(string)
  print string
  count1=0
  temp_str=""
  
  for i in string:
      temp_str+=i
      count1+=1
      if count1%8==0:
          print(temp_str)
          array1.append(int(temp_str,base=2))
          print (int(temp_str,base=2))
          print array1
          temp_str=""
  file2.write(array1)
  str_final=""
  for i in list:
      str_final+=str(i[0])+","+str(i[1])+","
  file2=open(filename+"k","w")
  file2.write(str_final)

  file2.close()


if __name__ == "__main__":
	if sys.argv[1] == 'compress':
		every_file(sys.argv[2])
	elif sys.argv[1] =='decompress':
		extract_dec(sys.argv[2])
#print(decode(str,list))

 


