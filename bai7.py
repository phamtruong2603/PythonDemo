from cmath import sqrt


def Tong(n):
    s = 0
    for i in range(1, n):
        if (n % i == 0):
            s += i
    return s

def check(n):
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0 and n % (i*i) == 0:
            return True
    return False

n = int(input())

if n == Tong(n) and check(n):
    print(0)
else:
    print(1)
     