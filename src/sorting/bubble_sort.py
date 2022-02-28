def bubble_sort():
	N=int(input())
	strok=input()
	mas=strok.split(' ')
	for i in range(N-1):
		for j in range(N-i-1):
			if mas[j]>mas[j+1]:
				mas[j], mas[j+1] = mas[j+1], mas[j]
				print(' '.join(map(strok, a)))

if __name__ == "__main__":
	bubble_sort()