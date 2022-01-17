from itertools import count
import math

def Function(n):
    a = []
    for i in range(2, int(math.sqrt(n))+1):
        while n % i == 0:
            if n % i == 0:
                n /= i
                a =a + [i]
    if n != 1:
        a = a + [int(n)]
    return a
    

t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    s = Function(n)
    length = len(s)

    print("1 * ", end="")
    for i in range(length-1):
        if s[i] != s[i+1]:
            print(s[i], "^", s.count(s[i]), sep='', end=" * ")
    print(s[length-1], "^", s.count(s[length-1]), sep='')
