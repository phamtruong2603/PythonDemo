def GCM(a, b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a

def coPrime(a, b):
    if GCM(a, b) == 1:
        return True
    return False

n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()

for i in range(n-1):
    for j in range(i+1, n):
        if coPrime(arr[i], arr[j]):
            print(arr[i], arr[j])
