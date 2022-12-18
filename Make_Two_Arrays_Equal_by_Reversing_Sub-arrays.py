def Equal(A, B, n):
  A.sort()
  B.sort()
  for i in range(n):
    if (A[i] != B[i]):
      return False
     
  return True
n=int(input())
A = list(map(int,input().split()))
m=int(input())
B = list(map(int,input().split()))
if (Equal(A, B, n)):
    print( "True")
else:
    print("False")