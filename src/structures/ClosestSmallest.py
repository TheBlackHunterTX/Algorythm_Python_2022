def ClosestSmallest():
    n = int(input())
    a = list(zip(list(map(int, input().split())), range(n)))
    tmp = []
    res = [0] * n
    for i in reversed(a):
        while tmp != [] and tmp[-1][0] >= i[0]:
            tmp.pop()
        if tmp == []:
            res[i[1]] = -1
        else:
            res[i[1]] = tmp[-1][1]
        tmp.append(i)
    print(*res)
ClosestSmallest()