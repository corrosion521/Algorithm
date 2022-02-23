'''
1. TypeError: 'int' object is not callable
=> 예약어를 변수명으로 사용하면 이렇게 됨
ex) max 를 변수명
'''
import sys

while True:
  l1 = (list(map(int,sys.stdin.readline().split())))
  l1.sort()

  if l1[0]==0 and l1[1]==0 and l1[2] == 0:
    break

  if l1[0]**2 + l1[1]**2 == l1[2]**2:
    print("right")
  else:
    print("wrong")