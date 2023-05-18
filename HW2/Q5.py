#!/usr/bin/python3
# HW2 _ Q5
"""
Recursive binary search algorithm using *args as func arguments
list of functions: binary_sarch, main .
"""

def binary_Search(x,*args ,L = 0 ,H = None ):
	"""
    searches for x argument inside args series of numbers, 
	while H and L are High and Low indexes respectively.
	returns index if found, and False if x doesn't exist in args.
    """
	if H == None:
		H = len(args) - 1

	if H < L:
		return -1

	mid = (L + H) // 2

	if args[mid] > x:
		return binary_Search(x, *args, L = L, H = mid-1)


	elif args[mid] < x:
		return binary_Search(x, *args, L = mid+1, H = H)

	else:
		return mid




def main():
	"""
	calling binary_search func on a series of numbers and showing
	the result.
	"""
	print('index:',binary_Search(1,1, 2, 3, 5, 7, 9, 11, 13))


if __name__ == '__main__':	
	main()

