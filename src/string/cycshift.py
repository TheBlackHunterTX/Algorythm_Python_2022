def shift(first, second):
    if second == first:
        return 0
    second *= 2
    p, m, q, xt = 13, 1, 2 ** 31 - 1, 1
    hash_first = 0
    hash_second = 0
    for i in first[::-1]:
        hash_first = (hash_first + ord(i) * m) % q
        m = (m * p) % q
    m = 1
    for i in second[:len(first)][::-1]:
        hash_second = (hash_second + ord(i) * m) % q
        m = (m * p) % q
    for i in range(len(first) - 1):
        xt = (xt * p) % q
    for i in range(1, len(second) - len(first) + 1):
        if hash_second == hash_first:
            return i - 1
        hash_second = p * (hash_second - ord(second[i - 1]) * xt)
        hash_second += ord(second[i + len(first) - 1])
        hash_second %= q
    return -1

def CycShift():
    print(shift(str(input()), str(input())))
CycShift()
