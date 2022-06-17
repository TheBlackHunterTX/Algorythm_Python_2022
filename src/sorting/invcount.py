def merge(A, B):
    res = []
    i = j = 0
    inv = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
            inv += (len(A) - i)
    res += A[i:]
    res += B[j:]
    return res, inv

def merge_sort_count(A):
    if len(A) <= 1:
        return A, 0
    mid = int(len(A) / 2)
    l, inv_l = merge_sort_count(A[:mid])
    r, inv_r = merge_sort_count(A[mid:])
    merged, inv = merge(l, r)
    inv += inv_l + inv_r
    return merged, inv

def task_merge_sort_count():
    n = int(input())
    print(merge_sort_count(list(map(int, input().split())))[1])
task_merge_sort_count()