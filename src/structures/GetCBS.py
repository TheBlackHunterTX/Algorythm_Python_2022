def CBS(string):
    arr = []
    count = 0
    for i in string:
        if i == '(':
            arr.append(i)
        elif arr != [] and arr[-1] == '(':
            arr.pop()
        else:
            count += 1
    return count + len(arr)

def FindCBS():
    print(CBS(str(input())))
FindCBS()