import io
import sys

_INPUT = """\
6
3 4 4
1 2 2
2 3 2
1 3 3
1 3 5
4 2 1 2
3 2 3
1 2 1
2 3 1
2 1 1
4 4 5
3 2 2
1 3 5
2 4 7
3 4 10
2 4 1 4 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M,K=map(int,input().split())
  edge=[]
  for _ in range(M):
    A,B,C=map(int,input().split())
    A-=1; B-=1
    edge.append((A,B,C))
  E=list(map(lambda x: int(x)-1,input().split()))
  inf=10**30
  D=[inf]*N
  D[0]=0
  for i in range(K):
    A,B,C=edge[E[i]]
    if D[B]>D[A]+C: D[B]=D[A]+C
  if D[-1]==inf: print(-1)
  else: print(D[-1])