a, K, N = list(map(int, input().split()))

i = a // K
j = N // K

if i >= j:
    print(-1)
else :
    for k in range(i , j+1):
        if K * k - a > 0:
         print(K * k - a, end=" ")