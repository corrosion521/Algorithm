'''
1. min() 내장함수 리스트에 적용 가능한거 까먹었다..
리스트 본질적인 형태 기억 ex) [1,2,3,4]
'''
x,y,w,h = map(int,input().split())

# # 가로 결정
# if w - x < x:
#     a = w - x
# else:
#     a = x
#
# # 세로 결정
# if h - y < y:
#     b = h - y
# else:
#     b = y
#
# # 가로vs세로
# if a > b:
#     print(b)
# else:
#     print(a)

print(min([x,y,h-y,w-x]))