import io
import re
import sys

_INPUT = """\
6
99
12
0
255
"""
sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  tmp='0123456789ABCDEF'
  N=int(input())
  print(tmp[N//16]+tmp[N%16])