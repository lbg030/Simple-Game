import pygame
#----------------------------------------------------------------#

# 기본 초기화 ( 반드시 해야 할 것들 )
pygame.init() # 반드시 해줘야 되는 부분

# 화면 크기 
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height)) # 480 * 640

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

#FPS
clock = pygame.time.Clock()

#--------------------------------------------------------#

# 1. 사용자 게임 초기화( 배경화면, 게임 이미지, 좌표, 속도, 폰트 등 )

running = True # 게임이 진행중인지 아닌지 확인하는거 = flag
while running :
    dt = clock.tick(60) #게임 화면의 초당 프레임 수를 설정
    # print("FPS : " + str(clock.get_fps())) # 프레임 확인
    
    # 2. 이벤트 처리 ( 키보드, 마우스 등 )
    for event in pygame.event.get(): # 어떤 이벤트가 발생하는지
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하면 ( 안쓰면 꺼지지 않음 )
            running = False

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리
    
    # 5. 화면에 그리기
    
    pygame.display.update() #게임 화면을 다시 그리기 ! (반드시 계속 호출 되어야 되는 부분)
    
# 파이게임 종료
pygame.quit()