import math

def GCD(a, b):
    if (b == 0):
        return a
    return GCD(b, a % b)

def Prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    k = 0
    for i in range(n):
        if GCD(n, i) == 1:
            k += 1
    if Prime(k):
        print("YES")
    else:
        print("NO")
    