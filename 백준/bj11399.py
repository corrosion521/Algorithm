'''
greedy
1.앞사람이 조금걸려야 뒷사람이 최소한으로 시간이 걸림
2.한 사람이 걸린 만큼 시간이 뒷사람들 모두에
영향을 주기에
3.따라서 정렬하여 앞에서부터 작은 수가 걸리도록 하면된다.
'''
l1= []
hap=0
result_list=[]

n = int(input())
l1=list(map(int,input().split()))
l1.sort()

for i in range(len(l1)):
  hap+=l1[i]
  result_list.append(hap)

print(sum(result_list))
