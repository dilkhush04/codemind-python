lst=[]
a=[]
r=0
n=int(input())
for i in range(n**2):
     if(i>1):
          c=0
          for j in range(2,int(i/2)):
               if(i%j==0):
                   c=c+1
          if(c==0):
               if(i<=n):
                   s=i
               else:
                    if(i>=n):
                         p=i
                         break
x=n-s
y=p-n
if(x<y):
     print(x)
elif(x==n):
     print(x)
else:
     print(y)