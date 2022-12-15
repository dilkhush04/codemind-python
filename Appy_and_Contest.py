def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a,a)
def lcm(a,b):
    return a/gcd(a,b)*b
T=int(input())
while(T>0):
    n,a,b,k=map(int,input().split())
    result=n//a+n//b+(2*(a*b/lcm(a,b)))
    if(result>=k):
        print("Win")
    else:
        print("Lose")