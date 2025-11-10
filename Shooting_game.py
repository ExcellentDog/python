
import pygame
import sys
pygame.init() # 파이게임 초기화

######
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)
pink = (255,100,215)
orange = (255,119,0)    
#####



w = 480 # 너비
h = 640 # 높이

pad = pygame.display.set_mode((w,h)) # 화면 생성
pygame.display.set_caption("2025") # 제목 설정

pad.fill(orange)


# 선그리기(위치, 색, 시작 좌표, 끝 좌표, 굵기)
'''
pygame.draw.line(pad,red,(240,0),(240,640),5)# (w/2,0),(w/2,640)
pygame.draw.line(pad,red,(0,213),(480,213),5)# (0,h/3),(480,h/3)
pygame.draw.circle(pad,yellow,(120,100),50,0)# 원 그리기 (위치, 색, 좌표, 지름, 테두리 굵기)
pygame.draw.circle(pad,yellow,(360,100),50,0)
pygame.draw.rect(pad,black,(70,400,340,200),0) #사각형 그리기 (위치, 색, (x좌표, y좌표, 가로길이, 세로길이), 테두리 굵기
pygame.draw.polygon(pad,pink,((100,300),(240,200),(380,300)))#다각형 그리기(위치,색,((좌표 1),(좌표 2),(좌표 3)....))
pygame.draw.ellipse(pad,pink,(300,300,100,50),0)#타원
'''
for x in range(0,481,80):
    for y in range(0,641,80):
        pygame.draw.circle(pad,yellow,(x,y),50)
for cx in range(0,481,int(480/6)):
    for cy in range(0,641,int(640/8)):
        pygame.draw.circle(pad,red,(cx,cy),45,10)

pygame.display.update() #화면 업데이트

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
