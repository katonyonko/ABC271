import io
import sys

_INPUT = """\
6
2 2
3 1 4 7
2 5 9
1 3
2 1
3 4
4 128 741 239 901
2 1 1
3 314 159 26535
1 1
2 2
3 3
1 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,Q=map(int,input().split())
  L=[list(map(int,input().split())) for _ in range(N)]
  for _ in range(Q):
    s,t=map(int,input().split())
    print(L[s-1][t])