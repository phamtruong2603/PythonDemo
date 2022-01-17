def check(arr, n, bArr) :
    arr.sort()
    bArr.sort()
    ok = True
    for i in range(n):
        if(arr[i] > bArr[i]):
            ok = False
            break
    if ok == True :
        return True
    return False

t = int(input())

while(t > 0) :
    t -= 1
    n = int(input())
    arr = [int(i) for i in input().split()]
    bArr = [int(i) for i in input().split()]
    if check(arr, n, bArr) :
        print("YES")
    else:
        print("NO")
    
