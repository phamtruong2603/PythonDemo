t = int(input())
while t > 0:
    t -= 1
    n, x, m = list(map(float, input().split()))
    count =0

    while n < m:
        n += (n*x/100)
        count += 1
    print(count)