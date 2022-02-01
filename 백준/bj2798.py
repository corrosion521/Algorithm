N,M = map(int,input().split()) #카드의 개수, 한도값

data = list(map(int,input().split())) # 카드 리스트

max = 0 # 카드 3장을 뽑아서 만드는 최대값
sum = 0 # 카드 3장의 합


for i in range(len(data)-2):# 첫 번째 카드 (뒤에 2개 제외 범위)
    for j in range(i+1,len(data)-1): # 두 번째 카드 (뒤에 1개 제외 범위, i보다 한 칸 앞)
        for k in range(j+1,len(data)): # 세 번째 카드 (끝까지, j보다 한 칸 앞)
            sum=data[i]+data[j]+data[k]
            if sum<=M and max<sum: # 3카드 합이 M보다 작거나 같고 동시에 이전 최대값을 갱신 가능한 경우
                max = sum

print(max)
