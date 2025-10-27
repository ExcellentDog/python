#turtle_shape.py
import random
import turtle as t

t.shape("turtle")
t.speed(0)
#1. 다각형 그리기
'''
n = int(input("몇 각형을 그릴까요? "))

for i in range(n):
    t.forward(100)
    t.left(360/n)

#2. 다각형 그리기 입력한 각형->삼각형까지 그리기

n = int(input("몇 각형부터 그릴까요? "))
t.shape("turtle")
t.speed(0)
for i in range(n,2,-1):
    for j in range(i):
        t.forward(100)
        t.left(360/i)
'''
#3. 다각형 그리고 색칠하기
'''
color = ["black","gray","brown","pink","purple","blue","green","yellow","orange","red","black","gray","brown","pink","purple","blue","green","yellow","orange","red"]


n = int(input("몇 각형부터 그릴까요? "))
t.shape("turtle")
t.speed(0)

for i in range(n,2,-1):
    t.color(color[i])
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()
'''

#다각형 그리고 랜덤 색칠하기
'''
color = ["black","gray","brown","pink","purple","blue","green","yellow","orange","red"]
    
n = int(input("몇 각형부터 그릴까요? "))
t.shape("turtle")
t.speed(0)

for i in range(n,2,-1):
    t.color(random.choice(color))#색깔 랜덤으로 고르기
    #random.shuffle(color)
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()

#5. 색 중복 없애기
color = ["black","gray","brown","pink","purple","blue","green","yellow","orange","red"]
    
n = int(input("몇 각형부터 그릴까요? "))#최대 색깔 리스트 변수 갯수
t.shape("turtle")
t.speed(0)

for i in range(n,2,-1):
    now_color = random.choice(color)#색깔 랜덤으로 고르기
    print(now_color)
    t.color(now_color)
    color.remove(now_color)
    #random.shuffle(color)
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()
'''
#6. 세가지 색깔이 계속 중복되어서 칠해지도록
# 각형제한없게
color = ["yellow","orange","red"]
count = 0
n = int(input("몇 각형부터 그릴까요? "))
t.shape("turtle")
t.speed(0)

for i in range(n,2,-1):
    if count == 3:
        count = 0
    t.color((color[count]))
    count += 1
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()
    
    

































    
