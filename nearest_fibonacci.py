n=int(input())
a=1
b=0
p=4
c=0
temp=c
for i in range(n**2):
     if(c<=n):
          s=c
     if(c>=n):
          p=c
          break
     c=a+b
     a=b
     b=c
if(s==n):
    print(s)
elif((n-s)<(p-n)):
    print(s)
elif((n-s)==(p-n)):
    print(s,p)
else:
    print(p)

   
                    
                
                    
        