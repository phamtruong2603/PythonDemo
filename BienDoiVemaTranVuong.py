def printArray(arr, n, m):
    for i in range(n) :
        for j in range(m) :
            print(arr[i][j], end = " ")
        print()

n, m = list(map(int, input().split()))

arr = []
for i in range(n):
    bArr = [int(i) for i in input().split()]
    arr = arr + [bArr]

if n > m:
    k = n-m
    del arr[0:k*2:2]
    printArray(arr, m, m)
else :
    k = m-n
    for i in range(n):
        del arr[i][1:k*2:2]
    printArray(arr, n, n)
