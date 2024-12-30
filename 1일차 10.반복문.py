#파이썬이 다른 언어와 차별되는 기능
#배열 : 동일한 데이터형의 값을 연속적으로 저장
#서로 다른 데이터형을 마음대로 사용 가능
#리스트 [값, 값, ...] : 연속적인 값을 삽입, 수정, 삭제 가능 ==> 배열과 비슷
#튜플 (값, 값, ...) : 연속적인 값을 이용만 가능 - 읽기용
#딕셔너리 {키:값,...} : 빈 연속적인 값을 삽입, 수정, 삭제 가능

#반복문(주어진 조건을 만족하는 동안 반복 수행)
#for 변수 in range(시작값, 끝값(전까지), 증가값):
#for i in range(0, 10, 1):  0으로 시작해서 1씩 증가하여 10전까지 반복 처리
#for 변수 in [리스트 값]: 변수에 리스트 값이 저장
#for i in [3,5,6] 리스트 값을 순서대로 읽어서 i에 저장해서 반복처리

#반복문에 사용하는 일반적인 변수명 : i, j, k, l, m, n
#초기값->조건->참이면 처리->증가값->조건

#1부터 100사이에 수 중에서 7의 배수만 출력하는 프로그램
for i in range(1, 101, 1):
    if i % 7 == 0:
        print(i,"는 7의 배수입니다.")

#구구단 프로그램(단수 2~9단, 차수 1~9)
dan = int(input("원하는 단수는?"))

for i in range(1, 10, 1):
    #print(dan, "*", i, "=", dan * i) #숫자값에 따라 모양이 깨짐

    # 모양 만들기->변수를 뒤에 뺀다.->뺀 변수 자리에 데이터형을 지정
    print("%3d * %3d = %3d" %(dan, i, dan*i))

#중첩 for문 : 일반 업무용에서 사용X, 수학, 그래픽, 게임 등에서는 많이 사용
#for i in range(시작, 끝, 증가): 반복 수가 끝 수 전까지 반복
#   for j in range(시작, 끝, 증가):  i*j 반복수를 한 만큼 반복
#i가 1회 처리시 j는 지정된 횟수만큼 반복처리
for i in range(0, 5, 1): #0,1,2,3,4 => 5회 반복, 총반복수 5회
    print("i=%3d" %i)
    #i=0, j=0~5 / i=1, j=0~5 / i=2, j=0~5
    for j in range(0, 5, 1): #0,1,2,3,4 => 5회 반복 총반복수 25회 반복
        print("j=%3d" % j)

#중첩 for문을 이용한 구구단(단수 2~9, 차수 1~9)
#2단 1~9, 3단 1~9, 4단 1~9, 5단 1~9,....,9단 1~9
#단수는 2~9 반복, 차수는 단수마다 1~9 반복
for i in range(2, 10, 1): #반복수가 적은 수, 단수
    for j in range(1, 10, 1): #반복수가 많은 수, 차수
        print("%3d * %3d = %3d" %(i, j, i*j))