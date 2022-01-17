t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    arr = [int(i) for i in input().split()]
    check = True
    k = 0
    while k < n:
        if arr.count(arr[k]) > n//2:
            print(arr[k])
            check = False
            break
        else:
            k = k + 1
    if check == True:
        print("NO")


# t = int(input())
# while t > 0:
#     t = t - 1
#     n = int(input())
#     a = [int(i) for i in input().split()]
#     ok = 0
#     k = 0
#     while k < n:
#         if a.count(a[k]) > n//2:
#             print(a[k])
#             ok = 1
#             break
#         else:
#             k = k + 1
#     if ok == 0:
#         print("NO")