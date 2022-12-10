def prime(n):
    if n<2:
        return 0
    for i in range(2,int(n/2)+1,1):
        if(n%i==0):
            return 0
    return 1
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if prime(i)==1:
            continue
        else:
            c=c+1
print(c)
            