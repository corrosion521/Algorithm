import math # 올림

# 규칙 : 달팽이가 높이 V미터인 나무막대올라감
# 낮에 A미터 up, 밤에 B미터 down . 정상에오르면 끝
# 다 오르려면 며칠?

# 입력: 세 정수 (A,B,V), 1<=B<A<=V<=10000000000
A,B,V = map(int,input().split())

day = 0
# 계산
if (V-B)%(A-B)==0:#한 번 도달하고 B만큼 내려갔을 때의 날짜 (도달했으므로 체크),딱 맞게 도달한 경우
    day  = ((V-B)/(A-B))
else: #날짜가 일부만 남을 수 없기에 올림,초과해서 도달한 경우
    day = ((V-B)/(A-B))

print(math.ceil(day)) #올림