

#제어문 연습 (중첩 if문) - 놀이동산 요금계산
'''
k = int(input('구분: 1.주간 2.야간\n'))
m = int(input('대상: 1. 대인 2. 소인\n'))

if k == 1: #주간
    if m == 1: #대인
        pay = 50000
    else: #소인
        pay = 40000
else: #야간
    if m == 1: #대인
        pay = 30000
    else: #소인
        pay = 20000
print(f'당신의 입장료는 {pay}입니다')
'''




'''
# for반복문
#2. 리스트 변수를 이용한 반복문
fruit = ['mango', 'apple' ,'orange' ,'kiwi', 'banana']
count = 0
# print(fruit[2])

for i in fruit:
    count += 1
    print(count,". ",i)
'''
'''
n = [0,1,2,3,4]
for i in n:
    print(i+1,". 안녕하세요")

'''
'''
food = ("치킨","삼겹살","피자","라면","짜장면","햄버거")

print(type(food))

for f in food:
    print(f)

'''
'''


for n in number:
    if n % 2 == 0:
        print(n,'는 짝수입니다.')
    else:
        print(f'{n} 는 홀수입니다.')
'''
'''
number = [273,103,5,32,65,9,72,880,99,58]
for n in number:
    print(f'{n}은 {len(str(n))}자릿수 입니다.')
'''


score_list = [98,58,65,78,44]
count = 0
total= 0 #합격한 친구들의 총점
count1 = 0 #합격한 친구들의 인원수
for score in score_list:
    count+=1
    if score >= 60:
        total += score
        print(f'{count}번 학생은 {score}점으로 합격입니다')
        count1 += 1
    else:
        print(f'{count}번 학생은 {score}점으로 불합격입니다')
print(f'총점은 {total}점 입니다.')

#합격한 친구들의 평균 점수를 구하세요

print(f"합격한 친구들의 총점은 {total}입니다.")
print(f'합격한 친구들의 평균은 {round(int(total)/int(count1),2)}입니다.')
    
















    
