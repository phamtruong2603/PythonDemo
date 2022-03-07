t = int(input())

while t > 0 :
    t -= 1
    str = input()
    count = 1
    for i in range(len(str)):
        
        if i == len(str) - 1:
            print(count, end="")
            print(str[i], end="")
        elif str[i] == str[i+1] :
            count += 1
        else :
            print(count, end="")
            print(str[i], end="")
            count = 1
    print("")