'''
구현 - 브루트 포스

1. 인풋 끊기
2. 단어 판별
3. 단어 뒤집기

!어려운점
1. 슬라이싱 했으면 더 편함
print(word[::-1])

'''
word=[]

tag_on=0
s = input() # 인풋 받기

# 인풋 검사
for i in s:
  if i == '<' : # 태그 진입 
    if len(word)>0: # 태그 출력 전에, 그 전의 word 우선 다 출력하기
      for i in range(len(word)-1,-1,-1): #거꾸로
        print(word[i],end='')
      word=[] # 출력했으니 초기화
    tag_on =1 # 태그 진입
    print("<",end='') # < 출력
  elif i == '>' : # 태그 닫기 
    tag_on = 0 # 끄기 
    print(">",end='') # 출력
    word=[] # 태그안의 단어 다 출력했으니 초기화

  elif i == ' ': # 공백있으면
    for i in range(len(word)-1,-1,-1): # 그전의 것 다 출력(역)
      print(word[i],end='')
    print(" ",end='') # 띄어쓰기
    word=[] # 출력했으니 초기화
  elif tag_on==1 and i!='<': # 태그 안인데, 아닌것이면 다 출력
    print(i,end='')
  else: # 태그 안의 것도 아니고, < > 도아니고 공백도 아니면 word에 집어넣음
    word.append(i)
# 나머지 것들 출력
if len(word)>0:
  for i in range(len(word)-1,-1,-1):
        print(word[i],end='')


  
 

