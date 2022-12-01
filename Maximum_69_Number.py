def number(n):
    num=0
    while n!=0:
        num=num*10+n%10
        n//=10
    return num
n=int(input())
s=0
c=0
n=number(n)
while(n!=0):
    rem=n%10
    if(c==0):
        if(rem==6):
            rem=9
            c=1
    s=s*10+rem
    n//=10
print(s)