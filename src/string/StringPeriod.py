def FindPrefs(string, length):
    prefs = [0] * length
    prefs[0] = 0
    for i in range(length - 1):
        j = prefs[i]
        while j > 0 and string[i + 1] != string[j]:
            j = prefs[j - 1]
        if string[i + 1] == string[j]:
            prefs[i + 1] = j + 1
        else:
            prefs[i + 1] = 0
    return prefs

def FindPeriod(string):
    length = len(string)
    prefs = FindPrefs(string, length)
    result = length - prefs[length - 1]
    if length % result == 0:
        return length // result
    return 1

def StringPeriod():
    print(FindPeriod(list(str(input()))))