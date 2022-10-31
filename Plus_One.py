n=int(input())
num=0
b=[]
a=list(map(int,input().split()))
for i in range(n):
    temp=a[i]
    num=num*10+temp
nnum=num+1
while(nnum!=0):
    rem=nnum%10
    b.append(rem)
    nnum=nnum//10
for i in range(len(b)-1,-1,-1):
    print(b[i],end=' ')
    
    