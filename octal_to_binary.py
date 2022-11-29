n=int(input())
num=0
i=0
a=[]
while(n!=0):
    rem=n%10
    num+=rem*8**i
    i=i+1
    n=n//10
while(num>0):
    c=num%2
    a.append(c)
    num//=2
for i in range(len(a)-1,-1,-1):
    print(a[i],end='')