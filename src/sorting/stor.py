def storage():
    s = input()
    Products = list(map(int, input().split()))
    s = input()
    Orders = list(map(int, input().split()))
    SortOrders = [0] * max(Orders)
    for J in Orders:
        SortOrders[J - 1] += 1 #Сортировка по типу продукта/количеству продупкта
    for i in range(len(Products)):
        if Products[i] >= SortOrders[i]:
            print('no')
        else:
            print('yes')
storage()   