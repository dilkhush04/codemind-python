n=int(input())
for i in range(1,n**2):
    num=2**i
    if(num<=n):
        s=num
    if(num>=n):
        p=num
        break
x=n-s
y=p-n
if(s==n):
    print(x)
elif(x<y):
    print(x)
else:
    print(y)

        
        