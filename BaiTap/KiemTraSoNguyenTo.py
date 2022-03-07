import math

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

n , m = list(map(int, input().split()))     
arr = []
for i in range(n) :
    bArr = list(map(int,input().split()))
    arr = arr + [bArr]
for i in range(n) :
    for j in range(m) :
        if prime(arr[i][j]) :
            arr[i][j] = 1
        else :
            arr[i][j] = 0
for i in range(n) :
    for j in range(m) :
        print(arr[i][j], end = " ")
    print()