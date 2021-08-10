#크로아티아 알파벳 집합
ca = ['c=','c-','dz=','d-','lj','nj','s=','z=']

#단어 입력
word = input()

#알파벳 집합을 돌려서 단어를 검사 후, 크로아티아 알파벳일 경우 단일 철자인 'a'로 변경
for i in ca:
    word=word.replace(i,'a')

#단어 길이 출력
print(len(word))