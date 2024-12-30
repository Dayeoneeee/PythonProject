#산술연산자
# =(대입 연산자), +(덧셈), -(뺄셈), *(곱셈), /(나눗셈),
# //(몫), %(나머지)-홀/짝수, ~ 배수, **(제곱)

#입력받은 수가 짝수인지 홀수인지를 판별하는 프로그램?
#분석 : 수동으로 동작->분석(반복 및 규칙)->프로그램(알고리즘)
#1/2=0,1  2/2=1,0  3/2=1/1  4/2=2,0  5/2=2,1  6/2=3,0
#몫은 짝/홀에 동일한 값이 존재
#나머지는 짝수는 0, 홀수는 1로 규칙
a = int(input("수를 입력하세요?")) #수를 입력받아서 정수형으로 변환

s = "" #블럭 밖에 선언(입력(선언)과 출력은 같은 위치)
if a % 2 == 0: #짝수인지 묻는 것
    s = "짝수"   #블럭안에 변수가
else: #홀수
    s = "홀수"

print("입력한 %d 수는 %s입니다." %(a,s)) #블럭박에서 사용할 때

#표준화 및 안정화 작업(중복코드 최소화)

#대입연산자(누적연산자)
#자신의 값으로 연산 후 결과를 자신에 다시 저장
#좌우 변수가 동일한 경우 사용
#a=a+1, b=b+c
#+=, -=, *=, /=, //=, %=, **=

#관계연산자
#두 값의 관계를 연산처리. 결과는 True, False
#==, !=, >, <, >=, <=

#논리연산자
#2개 이상의 관계연산자를 처리. 결과는 True, False
#and(&&) : 이고, 이면서, 모든 관계 연산자가 맞으면 true
#or(||) : 또는, 이거나, ~중, 관계연산자가 하나라도 맞으면 true
#not(!) : 결과를 반대로 출력

#비트연산자
#&(논리곱), |(논리합), ^(베타적 논리합), ~(부정), <<(왼쪽), >>(오른쪽)
#0,1로 구성 => 연산

#   [진리표]
#    A  B  &  |  ^
#    0  0  0  0  0
#    0  1  0  1  1
#    1  0  0  1  1
#    1  1  1  1  0