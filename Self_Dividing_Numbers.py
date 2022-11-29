def selfi(n):
    temp=n
    c=0
    k=0
    while(temp!=0):
        rem=temp%10
        c=c+1
        if(rem==0):
            break
        if(n%rem==0):
            k=k+1
        temp=temp//10
    if(c==k):
        return 1
    else:
        return 0
n=int(input())
m=int(input())
for i in range(n,m+1):
    if(selfi(i)==1):
        print(i,end=' ')
        