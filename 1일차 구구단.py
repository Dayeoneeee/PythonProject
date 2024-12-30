#2단부터 9단까지 가로로 출력하는 프로그램
#예) 2x1=2 3x1=3 4x1=4 5x1=5 6x1=6 7x1=7 8x1=8 9x1=9
#    2x2=4 3x2=6 4x2=8 5x2=10 6x2=12 7x2=14 8x2=16 9x2=18
#1행 단수(2~9), 차순 1
#2행 단수(2~9), 차순 2
#3행 단수(2~9), 차순 3

#콘솔은 위로 올라가는 기능이 없다.
for i in range(1,10,1) : #차순
    gugudan = "" #한 행을 처리할 변수, 1행 출력 후 초기 작업
    for j in range(2,10,1): #단수
        #1행을 작성하는 부분
        #문자열로 누적
        gugudan += str("%2d X %2d = %2d" % (j,i,i*j))+", "
        #print(gugudan) 안쪽 for 문으로 작업과정을 분석할 때
    print(gugudan) #for문 밖에 출력은 결과를 확인할 때

#for문으로 가로형 표기법
#while문으로 세로형 표기법

#while문 : 불규칙한 반복처리
#초기값
#while 조건:
#   증가값

#break : 남은 반복수와 상관없이 반복문을 종료
#continue : 현재 위치에서 반복문(조건식)으로 이동