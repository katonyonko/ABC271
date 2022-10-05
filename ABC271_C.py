import io
import sys

_INPUT = """\
6
6
1 2 4 6 7 271
10
1 1 1 1 1 1 1 1 1 1
1
5
5
2 2 3 4 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  N=int(input())
  A=list(map(int,input().split()))
  A.sort()
  B=deque([A[0]])
  tmp=0
  for i in range(N-1):
    if A[i]==A[i+1]: tmp+=1
    else: B.append(A[i+1])
  ans=0
  while B:
    x=B.popleft()
    if x==ans+1: ans+=1
    elif x<ans+1: tmp+=1
    else:
      B.appendleft(x)
      while len(B)>0 and tmp<2:
        y=B.pop()
        tmp+=1
      if tmp>1: tmp-=2; ans+=1
  ans+=tmp//2
  print(ans)