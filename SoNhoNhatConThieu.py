def check(arr, n):
    for i in range(n - 1):
        if arr[i+1] - arr[i] != 1:
            return arr[i] + 1
    return arr[n-1] + 1
n = int(input())

arr = [int(i) for i in input().split()]

arr = sorted(arr)
print(check(arr, n))
