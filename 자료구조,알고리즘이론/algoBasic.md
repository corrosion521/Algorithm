﻿
1. 알고리즘은 step by step으로 문제를 풀어나가는 로직이다.


2.[문제]-설계-> [알고리즘]-분석-> ((만족?))-yes->[프로그램]

< - -재설계 <-no

3. analysis(분석)을 통해 efficiency(효율)을 측정할 수 있다. 또 order(차수)를 통해서 이들을 분류할 수 있다.


4. 바람직한 알고리즘은 이해쉽고 명확해야한다. 또 당연히 효율적이어야 한다.



대표사진 삭제
알고리즘 수행시간

5. psedo code(의사코드)의 특징

1) 배열 인덱스 범위에 제한 없음

ex) S[1....n]// 다른 언어는 무조건 0부터 리스트,배열 시작

2) 프로시저의 파라미터에 2차원 배열 가변성

ex) void pname(A[][]){..} // 원래는 2차원 배열 파라미터에 행,렬 둘중하나는 있어야함

3) 지역배열에 변수 인덱스 허용

ex) keytype S[low..high];

4) 수학적 표현식허용 //≥ 이런거 쓸수 있다

5) bool, number(int float등),index(첨자)등 없는 타입 사용 가능.

6) repeat(n times){...}//반복

7)참조 파라미터(reference parameter)사용시 데이터타입 뒤에 &

ex) location& location


+ definition part : problem, in output 설명 기술

procedure part : 알고리즘 슈도코드 작성

﻿