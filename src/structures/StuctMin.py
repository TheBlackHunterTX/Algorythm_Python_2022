def push(stack, elem):
    stack.append(elem)
    return elem
def top(stack):
    return stack[-1]
def pop(stack):
    return stack.pop()
def size(stack):
    return len(stack)
def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(a * a, n // 2)
    else:
        return power(a, n - 1) * a
inf = 2 * power(10, 9) + 1
n, k = map(int, input().split())
a = [-inf] + list(map(int, input().split())) + [-inf]
stack = []
push(stack, 0)
ans = [0] * (n + 2)
for i in range(n + 2):
    while a[top(stack)] > a[i]:
        ans[pop(stack)] = i
    push(stack, i)
 
imin = 1
res = [0] * (n - k + 2)
for i in range(1, n - k + 2):
    if imin < i:
        imin = i
    while ans[imin] < i + k:
        imin = ans[imin]
    res[i] = imin
for i in range(1, n - k + 2):
    print(a[res[i]])