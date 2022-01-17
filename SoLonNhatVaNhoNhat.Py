while True :
    number = int(input())
    if number == 0: 
        break
    arr = []
    for i in range(number):
        bArr = int(input())
        arr = arr + [bArr]
    arr = sorted(arr)
    if arr[0] == arr[number-1]: 
        print("BANG NHAU")
    else: 
        print(arr[0], arr[number-1])