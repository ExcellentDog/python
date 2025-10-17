
# 제어문 - 선택문 반복문
# 반복문 for  range 문자열 리스트변수
# while
'''
i = 1
while i <=5:
    print(i,'안녕하세요')
    i= i+1
print('끝')


for i in range(1,6):
    print(i,'안녕하세요')
    i= i+1
print('끝')

i = 1
sum = 0
while i <=10:
    sum += i
    i += 1
print("1부터 10까지의 합: ",sum)

i = 3
while i <= 15:
    print(i)
    i = i+1
'''


#무한반복
'''
while True:
    score  = int(input("희망 영어 점수를 입력하세요 (0~100점): "))
    if score>=0 and score<=100:
        break
print("너는 영어시험에서 ",score,"점을 받을거야")
'''


'''
while True:
    num = int(input("숫자를 입력하세요(종료시 4입력): "))
    if num == 4:
        break
    else:
        print("당신이 입력한 수는 ",num,"입니다.")
'''
fruit = ['사과','용과','포도','망고']
for i in fruit:
    print(i)

i=0
while i<len(fruit):
    print(fruit[i])
    i += 1














