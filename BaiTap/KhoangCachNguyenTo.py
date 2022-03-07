import math

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

n, x = list(map(int, input().split()))
m = n
a = []
c = 1
while n > 0:
    c += 1
    if prime(c):
        a.append(c)
        n -= 1
print(x, end=' ')
for i in range(m):
    x += a[i]
    print(x, end=" ")
