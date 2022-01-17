t = int(input())

def snt(n):
    i = 2
    while i*i <= n:
        if n%i == 0:
            return 0
        i+=1
    return n>1

while t>0:
    n = int(input())
    a = [1]*n
    for i in range(2, n//2+1):
        if a[i] == 1 and n%i == 0:
            for j in range(i, n, i):
                a[j] = 0
    dem = 0
    for i in range(1, n):
        if a[i] == 1:
            dem += 1

    if snt(dem):
        print('YES')
    else:
        print('NO')
    t-=1
    