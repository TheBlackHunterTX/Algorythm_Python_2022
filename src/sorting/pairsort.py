def PairSort():
    num=int(input())
    mas=[]
    for h in range(num):
        mas.append(list(map(int, input().split())))
        #print(*mas)
    for i in range(len(mas)):
        elem=mas[i]
        j=i-1
        while j>=0 and compare(elem,mas[j]):
            mas[j+1]=mas[j]
            j-=1
        mas[j+1]=elem
    for elem in mas:
        print(*elem)
def compare(X,Y):
    if X[1]>Y[1]:
        return True
    else:
         if X[1]==Y[1]:
            return X[0]<Y[0]
         else:
            return False
PairSort()