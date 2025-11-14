
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

#####배경화면 넣기####
bg = pygame.image.load("images/background.jpg")
pad.blit(bg,(0,0))
p = pygame.image.load("images/alien.png")
px = w * 0.4
py = h * 0.9
pad.blit(p,(px,py))
pygame.display.update() #화면 업데이트

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
