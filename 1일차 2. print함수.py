#표준 출력장치 print()
print("문자열 출력")
print(123)
print("문자"+"문자열")
print(123+132)
#print(123+"문자열") #파이썬에서 + 연산자 사용시 좌우 데이터형이 동일해야만 한다.

#포맷 형식 %c, %s, %d, %i, %f
#%전체수.소숫점자리수 데이터형
#출력할 데이터형과 위치를 지정하고 값으로 대응
print("%d + %d" %(1220,300))    #인수값이 2개 이상이면(변수, 변수,...) ()안에
print("%d" %123)    #인수값이 하나이면 () 생략가능
print(123,23,34)
print(324,"연습","문자열")
print("01234")
print("%05d" %123)
print("%5d" %123)
print("%-5d" %123)