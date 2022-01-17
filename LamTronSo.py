t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if(n <= 9) :
        print(n)
    else :
        dem = 0 
        while(n > 9) :
            dem = dem + 1
            a = n%10
            n = n//10
            if a >= 5 :
                n+=1
        print(n*(10**dem))