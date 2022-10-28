n=int(input())
flag=0
rev=0
if(n>1):
    c=0
    for i in range(2,int(n/2)):
        if(n%i==0):
            c=1
    if(c==1):
        print("not prime")
    else:
        temp=n
        while(temp!=0):
            rem=temp%10
            rev=rev*10+rem
            temp=temp//10
        k=0
        for j in range(2,int(rev/2)):
            if(rev%j==0):
                k=1
        if(k==0):
            print("circular prime")
        else:
            print("prime but not a circular prime")
                
        
        

            