import re

t = int(input())

while t > 0:
    t -= 1
    str = input()
    arr = re.findall ( r'\d+' , str)
    for i in arr:
        str = str.replace(i,"")
    for i in range(len(str)):
        print(str[i] * int(arr[i]) , end="")
    print("")
