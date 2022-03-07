n = int(input())

while n > 0:
    n -= 1
    number = input()
    length = len(number)
    x = int(number[0])*10 + int(number[1])
    y = int(number[length-2])*10 + int(number[length-1])
    if x == y:
        print("YES")
    else:
        print("NO")