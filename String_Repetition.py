s=str(input())
n=int(input())
s=list(s)
c=s.count('a')
if(n%len(s)==0):
    res=n//len(s)
    print(res*c)
else:
    x=0
    res=n//len(s)
    res1=n%len(s)
    for i in range(res1):
        if s[i]=='a':
            x+=1
    print((res*c)+x)