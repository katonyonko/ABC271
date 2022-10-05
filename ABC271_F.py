import io
import sys

_INPUT = """\
6
3
1 5 2
7 0 5
4 2 3
2
1 2
2 1
10
1 0 1 0 0 1 0 0 0 1
0 0 0 1 0 1 0 1 1 0
1 0 0 0 1 0 1 0 0 0
0 1 0 0 0 1 1 0 0 1
0 0 1 1 0 1 1 0 1 0
1 0 0 0 1 0 0 1 1 0
1 1 1 0 0 0 1 1 0 0
0 1 1 0 0 1 1 0 1 0
1 0 1 1 0 0 0 0 0 0
1 0 1 1 0 0 1 1 1 0
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  N=int(input())
  A=[list(map(int,input().split())) for _ in range(N)]
  ans=0
  tmp1=[defaultdict(int) for _ in range(N)]
  tmp2=[defaultdict(int) for _ in range(N)]
  for k in range(1<<(N-1)):
    t=sum([1 for l in range(30) if (k>>l)&1==1])
    i,j=0,0
    s=A[i][j]
    for l in range(N-1):
      if (k>>l)&1==1: i+=1
      else: j+=1
      s^=A[i][j]
    tmp1[t][s]+=1
  for k in range(1<<(N-1)):
    t=sum([1 for l in range(30) if (k>>l)&1==1])
    i,j=N-1,N-1
    s=A[i][j]
    for l in range(N-2):
      if (k>>l)&1==1: j-=1
      else: i-=1
      s^=A[i][j]
    tmp2[t][s]+=1
  for i in range(N):
    for k in tmp1[i]:
      ans+=tmp1[i][k]*tmp2[i][k]
  print(ans)