import heapq

def walktree(heap,freq,code):
    # walkes through the tree and to find Huffman code of each character
    if(len(heap) == 1):
        times,charec = heap[0]
        freq[charec] = code
    else:
        char,child1,child2 = heap
        walktree(child1,freq,code+"0")
        walktree(child2,freq,code+"1")

def codemap(heap):
    freq = {}
    walktree(heap,freq,"")
    return freq

def maketree(list):
    heap = []
    for i in list:
       heapq.heappush(heap,[i])
    while (len(heap) > 1):
      child1 = heapq.heappop(heap)
      child2 = heapq.heappop(heap)
      comb_freq = child1[0][0] + child2[0][0]
      comb_char = child1[0][1] + child2[0][1]
      node = [(comb_freq,comb_char),child1,child2]
      heapq.heappush(heap,node)
    return heap.pop()