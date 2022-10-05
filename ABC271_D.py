import io
import sys

_INPUT = """\
6
3 11
1 4
2 3
5 7
5 25
2 8
9 3
4 11
5 1
12 6
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,S=map(int,input().split())
  dp=[[0]*(S+1) for _ in range(N+1)]
  dp[0][0]=1
  C=[list(map(int,input().split())) for _ in range(N)]
  for i in range(N):
    a,b=C[i]
    for j in range(S+1):
      if dp[i][j]==1:
        if j+a<=S: dp[i+1][j+a]=1
        if j+b<=S: dp[i+1][j+b]=1
  if dp[-1][S]==1:
    print('Yes')
    ans=[]
    for i in reversed(range(N)):
      a,b=C[i]
      if S-a>=0 and dp[i][S-a]==1:
        S-=a
        ans.append('H')
      else:
        S-=b
        ans.append('T')
    print(*ans[::-1],sep='')
  else: print('No')