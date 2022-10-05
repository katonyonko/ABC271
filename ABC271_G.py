import io
import sys

_INPUT = """\
6
1 50 50
ATATATATATATATATATATATAT
271 95 1
TTTTTTTTTTTTTTTTTTTTTTTT
10000000000000000 62 20
ATAATTATATTTAAAATATTATAT
10 20 30
AT
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  I=pow(100,mod-2,mod)
  def square(A,N):
    return [sum(A[i*N+k]*A[k*N+j] for k in range(N))%mod for i in range(N) for j in range(N)]
  def multi(A,B,N):
    return [sum(A[i*N+k]*B[k*N+j] for k in range(N))%mod for i in range(N) for j in range(N)]
  N,X,Y=map(int,input().split())
  c=input()
  M=[0]*(24**2)
  for i in range(24):
    l=[]
    tmp,tmp2=1,1
    for j in range(24):
      tmp=tmp2*(X*I if c[(i+j+1)%24]=='T' else Y*I)%mod
      tmp2=tmp2*((100-X)*I if c[(i+j+1)%24]=='T' else (100-Y)*I)%mod
      l.append(tmp)
    l=l[-(i+1):]+l[:-(i+1)]
    s=pow(sum(l),mod-2,mod)
    l=[l[j]*s%mod for j in range(24)]
    for j in range(24):
      M[j*24+i]=(M[j*24+i]+l[j])%mod
  mat=[1 if i==j else 0 for i in range(24) for j in range(24)]
  for i in range(61):
    if (N>>i)&1==1: mat=multi(mat,M[i*(24**2):(i+1)*(24**2)],24)
    M+=square(M[-(24**2):],24)
  print(sum(mat[i*24+23] for i in range(24) if c[i]=='A')%mod)