import math

def Prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def Sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s

t = int(input())
while t > 0:
    t -= 1
    a, b = list(map(int, input().split()))
    x = Sum(GCD(a, b))
    if Prime(x):
        print("YES")
    else:
        print("NO")
    
