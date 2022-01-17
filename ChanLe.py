import math
t = int(input())
while t > 0 :
    t -= 1
    s = input()
    i = 0
    sum = 0
    ok = 1
    n = len(s)
    for i in range(n-1) :
        a = int(s[i])
        b = int(s[i+1])
        if abs(a-b) != 2 :
            ok = 0
            break
        sum += a
    if(ok == 0): print("NO")
    else :
        sum += int(s[n-1])
        if(sum%10 == 0) : print("YES")
        else : print("NO")       