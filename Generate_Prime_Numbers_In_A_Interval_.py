x=int(input())
y=int(input())
for n in range(x,y+1):
    if(n>1):
        for j in range(2,int(n/2+1)):
            if(n%j==0):
                break
        else:
            print(n)