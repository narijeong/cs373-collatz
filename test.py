# Code to make meta cache in range of 1000 in 1-100000
from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

for x in range(1, 100000, 1000) :
	max = collatz_eval(x, x+999)
	#print(x, x+49) 
	print(max,",",end=" ")