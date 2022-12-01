def selfi(n):
    m=n
    c=0
    k=0
    while(m!=0):
        k=k+1
        rem=m%10
        if(rem==0):
            break
        else:
            if(n%rem==0):
                c=c+1
        m//=10
    if(c==k):
        return 1
    else:
        return 0
n=int(input())
m=int(input())
for i in range(n,m+1):
    if selfi(i)==1:
        print(i,end=" ")