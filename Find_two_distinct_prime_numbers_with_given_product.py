def prime(n):
    if n<2:
        return 0
    for i in range(2,int(n/2)+1,1):
        if(n%i==0):
            return 0
    return n
n=int(input())
k=0
for i in range(n):
    for j in range(i+1,n):
        if(prime(i)*prime(j)==n):
            k=1
            print(i,j)
if(k==0):
    print("-1")
            