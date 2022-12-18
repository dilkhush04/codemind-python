n=int(input())
start=list(map(int,input().split()))
m=int(input())
end=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n):
    if k>=start[i] and k<=end[i]:
        c=c+1
print(c)