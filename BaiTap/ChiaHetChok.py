a, k, n = list(map(int, input().split()))

x = n / k
y = a / k + 1

if y >= x:
    print(-1)
else:
    for i in range(int(x)):
        print(int((i*k)+a))

