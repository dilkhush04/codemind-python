def reverse(n):
    rev=0
    temp=n
    while(temp!=0):
        rem=temp%10
        rev=rev*10+rem
        temp=temp//10
    return rev
n=int(input())
n=n+reverse(n)
while(1>0):
    if(n==reverse(n)):
        print(n)
        break
    else:
        n=n+reverse(n)