'''
1. dict :
1) { } 로 초기화
2) d1[키] = 값 . 형식으로 만들어나가면됨.
빈 사전 만들고 계속 넣기 가능.
3) 값으로 키만을 뽑아낼 수 없음.. 찾아봤는데 모르겠음..
=> 이런 경우 그냥 값으로 쓰인 걸 키<->값으로 뒤바꿔서 새로운 dict를 만드는 것도 하나의 방법이다.
4) index() : 해당리스트를 처음부터 다 뒤짐. 리스트의 탐색은 시간복잡도 O(N)
=> dictionary는 시간복잡도 O(1)임.
=> 따라서 인덱스 탐색, 특정 문자 탐색에는 dictionary가 유리. 말그대로 딕셔너리
2. isdigit(): 문자열이 모두 숫자로 구성되어 있는지 판별. 모두 숫자면 true,아니면 false
'''
import sys

n,m = map(int, sys.stdin.readline().split())

d1 = {} # 도감: 키가 숫자
d2 = {} # 도감: 키가 한글

for i in range(n):#포켓몬 수
    tmp= sys.stdin.readline().strip()
    d1[i]=tmp # 각 번호에 맞게 넣기
    d2[tmp]=i+1 # 각 번호에 맞게 넣기,단 인덱스 고려해서 +1


for i in range(m):
    a = sys.stdin.readline().strip()

    if a.isdigit(): # 숫자면 true->키가 숫자인 d1도감
        print(d1[int(a)-1]) # 포켓몬 이름 출력 , 인덱스라 0부터 인것 고려
    else:
        # 아니면 키가 이름인 d2도감
        print(d2[a]) # 포켓몬 넘버 출력