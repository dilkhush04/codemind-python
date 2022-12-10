def prime(n):
    if n<2:
        return 0
    for i in range(2,int(n/2)+1,1):
        if(n%i==0):
            return 0
    return 1
n=int(input())
if prime(n)==1:
    print("prime")
else:
    print("not a prime")
            