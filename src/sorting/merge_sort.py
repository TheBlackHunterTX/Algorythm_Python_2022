def Merge(A, B):
    result = []
    i=j=0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    result += A[i:]
    result += B[j:]
    return result
def MergeSort(A,start, end):
    if (end-start) == 1:
        return A[start:end]
    middle = int((start+end)/2)
    l=MergeSort(A, start, middle)
    r=MergeSort(A, middle,end)
    merged=Merge(l,r)
    print(start+1, end, merged[0], merged[-1])
    return merged
def task_merge_sort():
    n = int(input())
    print(*MergeSort(list(map(int, input().split())), 0, n))
task_merge_sort()