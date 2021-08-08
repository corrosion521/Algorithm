
#판별함수 : 그룹단어여부 (한번 쓰인 철자가 연속한 경우를 제외하고 또 다시 쓰인 경우는 제외)
def groupword(word):
    jd = []  # 판별리스트
    for i in range(len(word)):
        if word[i] not in jd:#jd에 철자가 없는 경우
            jd.append(word[i])
        else :
            if word[i-1]==word[i]:#jd에 철자가 있으나 연속되어 있는 경우
                jd.append(word[i])
            else:
                return 0
    return 1

#입력 : 단어 x N개
N = int(input())
sum = 0#그룹단어의 개수
for i in range(N):
    word = input()
    sum+=groupword(word)

print(sum)