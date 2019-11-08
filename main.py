import os
import heapq 
import sys


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

def decode(code,list):
   decoding=""
   codetree=fulltree=maketree(list)
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




# files=os.listdir(os.getcwd())
# for i in files:
#   file = open(i, 'r')
#   text=file.read()
def encode(filename):
  file=open(filename,"r")
  text=file.read()
  print(len(text)*8)

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

  heap = maketree(list)
  freq = codemap(heap)
  print(freq)
  
  
  str=""
  for j in text:
    str+=freq[j]
#import tarfile
  binary=(bin(int(str,base=2)))
  print binary
  file2=open("hi1","wb")
  file2.write(binary)
#   tar = tarfile.open("hi", "w:gz")
#   tar.add("hi")
  file2.close()


if __name__ == "__main__":
	if sys.argv[1] == 'compress':
		encode(sys.argv[2])
	elif sys.argv[1] =='decompress':
		decode(sys.argv[2])
#print(decode(str,list))

 


