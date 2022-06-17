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
    num = int(input())
    mas = list(map(int, input().split()))
    swpd=0
    for i in range(num-1):
        for j in range(num-i-1):
            if mas[j] > mas[j + 1]:
                mas[j], mas[j + 1] = (mas[j + 1], mas[j])
                swpd += 1
                print(*mas)
    if swpd == 0:
        print(0)
bubble_sort()