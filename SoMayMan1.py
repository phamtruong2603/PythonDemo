number = input()

x1 = number.count("4")
x2 = number.count("7")

if x1+x2 == 4 or x1+x2 == 7:
    print("YES")
else:
    print("NO")