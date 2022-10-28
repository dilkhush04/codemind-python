num=int(input())
lst=[]
a=[]
r=0
for i in range(num):
    lst.append(int(input()))
for k in range(num):
    n=lst[k]
    for i in range(n**2):
        if(i>1):
            c=0
            for j in range(2,int(i/2)):
                if(i%j==0):
                    c=c+1
            if(c==0):
                if(i<=n):
                    s=i
                else:
                    if(i>=n):
                        p=i
                        break;
    if(s==n):
        max=s
    elif((n-s)>(p-n)):
        max=p
    else:
        max=s
    a.append(max)
    r=r+1
for i in range(r):
    print(a[i])
    
    
                    
                
                    
        