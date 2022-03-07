t = int(input())
while t > 0:
    t -= 1
    n = input()
    s = 1
    length = len(n)
    for i in range(length):
        if n[i] > "1":
            s *= int(n[i])
    print(s)