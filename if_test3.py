import random

#제어문-선택문 if  if~else     If~elif~else
'''
#홀짝구하기      % 2

num = 150
if num % 2 == 0:#짝수일때
    print("짝수입니다")
else:
    print("홀수입니다")

# 학점구하기
score = int(input("성적을 입력하세요: "))
if score >= 90:
    print("A학점 입니다")
elif 90 > score >= 80:
    print("B학점 입니다")
elif 80 > score >= 70:
    print("C학점 입니다")
elif 70 > score >= 60:
    print("D학점 입니다")
else:
    print("F학점 입니다")
'''


#1부터 6까지 적힌 주사위 두개를 던져 나오는 값을 a, b라고 할때
a = random.randint(1,6)
b = random.randint(1,6)
print("첫번째 주사위의 값은: ",a)
print("첫번째 주사위의 값은: ",b)

if a %2 == 1 and b %2 == 1:
    print(a**2 + b)#pow(a,2)
elif a %2 == 0 and b %2 == 0:
    print(abs(a-b))
else:
    print(2*(a+b))
