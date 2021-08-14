'''
출처: 인프런 강의

지구에서 제일 쉽게 설명한 자료구조와 알고리즘- 개복치 개발자

수업 때 들은 내용을 바탕으로 간략하게 요약한 내용입니다. 틀린 내용이 있거나 고쳐야 할 점이 있다면 가르쳐주신다면 감사하겠습니다.

문제가 될 시 바로 게시글 내리도록 하겠습니다.

﻿https://www.inflearn.com/course/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-1/dashboard

'''


hash_table =[[] for _ in range(10)]#10x? 이차원 리스트 생성
print(hash_table)
# output:
#[[],[],[],[],[],[],[],[],[],[]]

#삽입
def insert(hash_table,key,value):
    # key값 설정
    hash_key = key % len(hash_table)

    #중복 확인을 위한 애
    key_exists = False
    bucket = hash_table[hash_key]

    # bucket안에 여러개가 들어있으면 반복문으로 돌리면서 확인
    for i,kv in enumerate(bucket):
        #kv(Key,value)
        k,v = kv
        if key == k:
            # 중복을 확인했다면 if else중 if로 가기
            key_exists = True
            break
    # 중복되는 것이 있을 땐 not append
    if key_exists:
        bucket[i] = ((key,value))
    # 중복되는 것이 없으면 append
    else:
        bucket.append((key,value))

insert(hash_table,100,'민수')
insert(hash_table,105,'철수')
insert(hash_table,200,'민지')

insert(hash_table,200,'민지')
print(hash_table)
#[[(100, '민수'), (200, '민지')], [], [], [], [], [(105, '철수')], [], [], [], []]
