n=int(input())
num=1
for i in range(n*n):
    num=i
    rev=0
    while(num):
        rem=num%10
        rev=rev*10+rem
        num//=10
    if(i==rev):
        if(i<n):
            min=i
        if(i>n):
            max=i
            break
x=n-min
y=max-n
if(x==y):
    print(min,max)
elif(x<y):
    print(min)
else:
    print(max)