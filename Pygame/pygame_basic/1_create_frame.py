import pygame
pygame.init() # 반드시 해줘야 되는 부분

# 화면 크기 
screen_width = 480 # 가로
screen_height = 640 # 세로
screeen = pygame.display.set_mode((screen_width, screen_height)) # 480 * 640

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

# 이벤트 루프
running = True # 게임이 진행중인지 아닌지 확인하는거 = flag
while running :
    for event in pygame.event.get(): # 어떤 이벤트가 발생하는지
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하면 ( 안쓰면 꺼지지 않음 )
            running = False
# 파이게임 종료
pygame.quit()