import math

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

n = int(input())
arr = [int(i) for i in input().split()]
for i in range(n):
    check = True
    for j in range(i):
        if arr[i] == arr[j]:
            check = False
            break
    if check and prime(arr[i]):
        print(arr[i], arr.count(arr[i]))