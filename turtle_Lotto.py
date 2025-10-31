import turtle as t
import random
#통에 공을 넣는다(1~45)
'''
lotto_num = [1,2,3,4,5,6,7,8,9,10,
             11,12,13,14,15,16,17,18,19,20,
             21,22,23,24,25,26,27,28,29,30,
             31,32,33,34,35,36,37,38,39,40,
             41,42,43,44,45]
'''
lotto_num = []
for n in range(1,46):
    lotto_num.append(n)
    #print(lotto_num)
#공 섞기
random.shuffle(lotto_num)
#print(lotto_num)
'''
num1 = lotto_num[0]
num2 = lotto_num[1]
num3 = lotto_num[2]
num4 = lotto_num[3]
num5 = lotto_num[4]
num6 = lotto_num[5]
print(f'첫번째 공 = {num1}')
print(f'두번째 공 = {num2}')
print(f'세번째 공 = {num3}')
print(f'네번째 공 = {num4}')
print(f'다섯번째 공 = {num5}')
print(f'여섯번째 공 = {num6}')
'''

#제목
t.shape("turtle")
t.hideturtle()
t.speed(5)#0~10 가장 빠른 0 10 9 8 7...
s = t.Screen()
s.bgcolor("black")
t.goto(0,150)
t.color("white")
t.write("로또 번호 생성기",align = "center", font=("Impact",90,"bold"))
t.penup()
color = ["red","blue","yellow"]
count = 0
for i in range(-500,501,200):
    t.penup()
    t.goto(i, -100)
    t.pendown()
    t.color(random.choice(color))
    t.begin_fill()
    t.circle(80,360)
    t.end_fill()
    t.color("white")
    t.write(lotto_num[count],align = "center", font=("Impact",90,"bold"))
    count += 1
