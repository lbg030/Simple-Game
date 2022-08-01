import pygame
pygame.init() # 반드시 해줘야 되는 부분

# 화면 크기 
screen_width = 480 # 가로
screen_height = 640 # 세로
screeen = pygame.display.set_mode((screen_width, screen_height)) # 480 * 640

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름
