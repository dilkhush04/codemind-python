def number(n):
    num=0
    while(n!=0):
        num=num*10+n%10
        n=n//10
    return num
n=int(input())
n=number(n)
c=0
num=0
while(n!=0):
    i=n%10
    if(c==0):
        if(i==6):
            i=9
            c=5
    num=num*10+i
    n=n//10
print(num)
    