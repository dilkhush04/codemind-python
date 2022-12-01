n=int(input())
s=0
m=n**2
while(m!=0):
    s+=m%10
    m//=10
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")
    
