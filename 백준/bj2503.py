'''
구현-브루트포스

1. 두 가지 케이스 비교
2. 볼, 스트라이크 두 조건 검사

!몰랐던 점
1. 브루트포스 :
1) 예비후보들->ex)for i in range(111,999)처럼 다돌리기
2) 당연하지만, 그런 와중에 조건문을 통해 걸러내야함 -ex) 0들어간 경우, 중복된 경우
2.str화: f"{ori}"
'''

# baseball check  : 답 후보 vs 테스트 케이스 1
def baseball(ori,sub):
  s,b=0,0
  str_ori = f"{ori}"
  str_sub = f"{sub}"

  for i in range(len(str_ori)):
    if str_ori[i] == str_sub[i]: # 스트라이크면 s증가
      s+=1

    elif str_sub[i] in str_ori: # 스트라이크는 아니지만 있으면 b증가
      b+=1

  return s,b

n = int(input()) # 테스트 케이스 개수 입력

num_lines= [] # 테스트케이스 리스트

answers = [] # 답 들 

# 테스트 케이스 입력
for i in range(n):
  num_lines.append(list(map(int,input().split())))

# ! 답 후보들 돌리기(3자리수,0안들어감,중복x)
for num in range(111,1000):
  str_num = f"{num}"
  if "0" in str_num: #! 브루트 포스 걸러내기 1:0 들어간 경우.
    continue

  twice_check =False # ! 브루트포스 걸러내기 2: 중복 체크.
  # 2중 for문을 통해서 3글자 전부 검사 
  for i in range(len(str_num)):
    for j in range(i+1,len(str_num)):#기준값도 움직여야하니..
      if str_num[i] == str_num[j]:
        twice_check =True # 중복값 존재시 true
        break

    if twice_check: # true니까 
      break
  
  if twice_check:#메인 계산(base ball check)안하고 continue
    continue

  # 이제 답 후보들 검사 
  check = False# 테스트 케이스 만족 초기값
  for i in range(len(num_lines)):
    s,b = baseball(num,num_lines[i][0])# 후보num vs 테스트케이스 

    if s == num_lines[i][1] and b == num_lines[i][2]: # 테스트케이스 만족 
      check = True
    else: #만족하지 않으면 (테스트케이스 하나라도 )
      check =False
      break

  if check :  # 전부 통과시 리스트 추가
    answers.append(num)

print(len(answers))
  
