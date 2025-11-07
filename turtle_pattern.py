from turtle import *   # turtle 모듈의 모든 함수와 클래스를 불러온다.
import random
speed(0)               # 거북이의 그리기 속도를 최대로 설정 (0이 가장 빠름)
pensize(3)
col = ['red','orange','yellow','green','blue','purple']
random.shuffle(col)
bgcolor(col[2])
color(col[0],col[1]) # 선(line) 색은 'red', 내부 채움(fill) 색은 'yellow'로 설정
begin_fill()           # 이후 그려질 도형의 내부 색 채우기 시작을 알림

while True:            # 무한 반복문 시작
    forward(10)       # 거북이가 10픽셀 앞으로 이동
    left(20)        # 거북이를 왼쪽으로 20도 회전
    circle(random.randint(100,200))
    # 이 각도를 170도로 한 이유:
    # 360의 약수가 아니기 때문에 회전하면서 점점 중심으로 수렴하며
    # 마치 별 모양의 나선 같은 무늬가 생긴다.

    if abs(pos()) < 1: # 현재 거북이의 위치(pos())가 (0,0) 근처라면
        break           # 원점으로 거의 돌아왔다는 뜻 → 반복 종료

end_fill()             # 도형 내부 색 채우기 종료
done()                 # 그리기 종료, 창을 닫지 않고 유지
