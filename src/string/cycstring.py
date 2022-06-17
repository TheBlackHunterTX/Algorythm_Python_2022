def FindPrefs(string, length):
    prefs = [0] * length
    for i in range(length - 1):
        j = prefs[i]
        while j > 0 and string[i + 1] != string[j]:
            j = prefs[j - 1]
        if string[i + 1] == string[j]:
            prefs[i + 1] = j + 1
        else:
            prefs[i + 1] = 0
    return prefs

def CycString():
    string = list(str(input()))
    length = len(string)
    prefs = FindPrefs(string, length)
    print(length - prefs[-1])
CycString()