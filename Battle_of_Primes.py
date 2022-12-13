def Battle(n):
    c=0
    for i in range(1,n+1,1):
        if(n%i==0):
            c=c+1
    if(c==2):
        return 1
    else:
        return 0
day1=int(input())
day2=int(input())
day3=99
for i in range(1,day3+1):
    if Battle(day1+day2+i)==1:
        print(i)
        break

    