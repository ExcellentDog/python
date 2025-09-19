#반올림 round 포매팅
'''
print(round(5.5795,2))#5.58
print(round(5.5295,1))#5.5
print(round(5.5295,0))#6.0
print(round(5.5295,-1))#10
print(round(5.5295))#6
a =round(5.5295)
b =round(5.5295,0)
print(type(a))#int
print(type(b))#float

#포매팅
print("{:.1f}".format(3.5289))
print("{:.0f}".format(3.5289))
print("{:.3f}".format(3.5289))#3.529

print("{0}과 {0}".format(3.5555,3.7777))#인덱스
print("{:.2f}과 {:.1f}".format(3.5555,3.7777))
print("{1:.1f}과 {0:.2f}".format(3.5555,3.7777))

a = 5
b = 8
if a >=b:
    print(a+b)
else:
    print(a*b)

money = int(input("가지고 있는 돈은 얼마인가요?"))

if money>=20000:
    print("탕수육 먹어요")
elif 20000>money>=10000:
    print("쟁반짜장 먹자")
elif 10000>money>=8000:
    print("해물짬뽕 어때")
elif 6000>money>=4000:
    print("짜장면 먹지뭐")
else:
    print("단무지나 먹어야겠다")

yellow_card = int(input("누적 파울 수 입력 "))
foul = input("이번 판정결과 ")
if foul:
    yellow_card +=1
    if yellow_card ==2:
        print("경고 누적 퇴장")
    else:
        print("휴~ 조심하자")
else:
    print("경고")

score = [85, 92, 78, 95, 88]
print(f"입력된 점수:{score}")
print(f"전체 학생수:{len(score)}명")
print(f"최고 점수:{max(score)}점")
print(f"최저 점수:{min(score)}점")
print(f"총합 점수:{sum(score)}점")
print("평균점수:",sum(score)/len(score),"점")
'''
score = [85, 92, 78, 95, 88]
print("입력된 점수:",score)
print("전체학생수:",len(score),"명")
if len(score)>0:
    max_score = max(score)
    min_score = min(score)
    tot_score = sum(score)
    avg_score = sum(score)/len(score)
    print(f"최고 점수:{max_score}점")
    print(f"최저 점수:{min_score}점")
    print(f"총합 점수:{ tot_score}점")
    print("평균점수:{:.2f}점".format(avg_score))
else:
    print("입력된 점수가 없습니다.")
                                         







