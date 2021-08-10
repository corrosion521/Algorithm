
#판별함수 : 그룹단어여부 (한번 쓰인 철자가 연속한 경우를 제외하고 또 다시 쓰인 경우는 제외)
def groupword(word):
    for i in range(len(word)-1):
        if word.find(word[i])>word.find(word[i+1]):#find는 그 인자가 처음 등장한 인덱스를 반환하는데, 이 때 이 경우는 뒤에나온 철자가 사실은 앞에서 한 번 나왔다는 것이다.
            return 0
    return 1

#입력 : 단어 x N개
N = int(input())
sum = 0#그룹단어의 개수
for i in range(N):
    word = input()
    sum+=groupword(word)

print(sum)