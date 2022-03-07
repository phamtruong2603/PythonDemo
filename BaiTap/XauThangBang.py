import math
def check(n , str):
    for i in range(1,n):
        if abs(ord(str[i]) - ord(str[i-1])) != abs(ord(str[n-i-1]) - ord(str[n-i])):
            return False
    return True
t = int(input())

while t > 0:
    t -= 1
    str = input()
    length = len(str)

    if check(length, str):
        print("YES")
    else:
        print("NO")
