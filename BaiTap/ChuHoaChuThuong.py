str = input()

count = 0
count1 = 0

for s in str :
    if s >= 'A' and s <= 'Z':
        count += 1
    else : 
        count1 += 1
    
if(count > count1):
    print(str.upper())
else:
    print(str.lower())