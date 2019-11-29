import os
import heapq 
import sys
import struct
from trees      import *
from compress   import *
from decompress import *

if __name__ == "__main__":
	if sys.argv[1] == 'compress':
		every_file( sys.argv[2] )
	elif sys.argv[1] =='decompress':
		every_file_de( sys.argv[2] )


 


