t = int(input())
while t > 0:
    t -= 1
    number = input()

    x1 = number.count("4")
    x2 = number.count("7")

    if x1+x2 == len(number):
        print("YES")
    else:
        print("NO")