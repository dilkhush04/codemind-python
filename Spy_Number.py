n=int(input())
p=1
s=0
while(n!=0):
    s+=n%10
    p=p*n%10
    n//=10
if(s==p):
    print("Spy Number")
else:
    print("Not Spy Number")