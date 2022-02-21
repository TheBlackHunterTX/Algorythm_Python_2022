"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join(['4','4 3 2 1']))  # input
>>> bubble_sort()
3 4 2 1
3 2 4 1
3 2 1 4
2 3 1 4
2 1 3 4
1 2 3 4
"""

def bubble_sort():
	n=int(input())
	z=input()
	a=z.split(' ')
	for i in range(n-1):
		for j in range(n-i-1):
			if a[j]>a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
				print(' '.join(map(str, a)))
	'''print(' '.join(map(str, a)))'''

if __name__ == "__main__":
	bubble_sort()
