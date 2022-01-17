t = int(input())
while t > 0:
    t -= 1
    n = input()
    n = list(n)
    length = len(n)
    check = True
    for i in range(length-1, 0, -1) :
        if check == False:
            break
        if n[i] <= n[i-1] :
            for j in range(length-1, i-1, -1):
                if n[j] < n[i-1] and n[j] != n[j-1]:
                    temp = n[i-1]
                    n[i-1] = n[j]
                    n[j] = temp
                    check = False
                    break

    if check or n[0] == "0":
        print(-1)
    else:
        print("".join(n))
