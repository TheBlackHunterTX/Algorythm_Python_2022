"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join([\
'1',\
'1'\
]))
>>> task_merge_sort()
1
>>> sys.stdin = io.StringIO(chr(10).join([\
'2',\
'3 1',\
]))
>>> task_merge_sort()
1 2 1 3
1 3 
>>> sys.stdin = io.StringIO(chr(10).join([\
'5',\
'5 4 3 2 1',\
]))
>>> task_merge_sort()
1 2 4 5
4 5 1 2
3 5 1 3
1 5 1 5
1 2 3 4 5 
>>> print(merge([2,3,4],[1,2,3]))
[1, 2, 2, 3, 3, 4]
"""
def merge(A, B):
    res = []
    count = 0 
    count1 = 0
    while count < len(A) and count1 < len(B):
        if A[count] <= B[count1]:
            res.append(A[count])
            count += 1
        else:
            res.append(B[count1])
            count += 1
    res += A[count:]
    res += B[count1:]
    return res

def merge_sort(A, b, e):
    if (e - b) == 1:
        return A[b:e]
    m = int((b + e) / 2)
    l = merge_sort(A, b, m)
    r = merge_sort(A, m, e)
    mrg = merge(l, r)
    print(b + 1, end, mrg[0], mrg[-1])
    return mrg

def task_merge_sort():
    n = int(input())
    print(*merge_sort(list(map(int, input().split())), 0, n))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)