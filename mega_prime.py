def mega(n):
    if(n==1):
        return 0
    for i in range(2,int(n**0.5)+1,1):
        if(n%i==0):
            return 0
    return 1
n=int(input())
k=0
if mega(n)==1:
    while(n!=0):
        k=1
        if(mega(n%10)==0):
            print("Not Mega Prime")
            k=2
            break
        n//=10
    if(k==1):
        print("Mega Prime")
if(k==0):
    print("Not Mega Prime")

    