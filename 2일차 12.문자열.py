# 문자열은 리스트 비슷하게 처리
# 리스트 : [] 사용, 문자열 "",'' 사용
# 슬라이딩 및 첨자 사용이 가능
ss = "파이썬 프로그램"

print(ss[0])
print(ss[3:])
print(ss[::-1])
print(ss[:5])

# 모든 컴퓨터 언어에는 문자열이 없다.
# 문자만 존재 -> 배열에 저장 -> 연속 출력(문자열)

# 문자열 추가는 +를 이용
ss = ss+"추가된 문자열"

for i in range(0,len(ss)): #문자열을 길이만큼 반복처리
    print(ss[i], '$', end='') #한문자씩 출력
